// ===== ESSENTIAL FUNCTIONS ONLY =====

// Global variables
let users = JSON.parse(localStorage.getItem('busbd_users')) || [];
let currentUser = JSON.parse(localStorage.getItem('busbd_current_user')) || null;

// 1. MODAL FUNCTIONS
function showLoginModal() {
    console.log('Opening login modal');
    const modal = document.getElementById('loginModal');
    if (modal) {
        modal.style.display = 'block';
        document.body.style.overflow = 'hidden';
    }
}

function showRegisterModal() {
    console.log('Opening register modal');
    const modal = document.getElementById('registerModal');
    if (modal) {
        modal.style.display = 'block';
        document.body.style.overflow = 'hidden';
    }
}

function closeModal(modalId) {
    console.log('Closing modal:', modalId);
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.style.display = 'none';
        document.body.style.overflow = 'auto';
    }
}

function switchToRegister() {
    closeModal('loginModal');
    showRegisterModal();
}

function switchToLogin() {
    closeModal('registerModal');
    showLoginModal();
}

// 2. AUTHENTICATION FUNCTIONS
function handleLogin(event) {
    event.preventDefault();
    console.log('Handling login');
    
    const email = document.getElementById('loginEmail')?.value;
    const password = document.getElementById('loginPassword')?.value;
    
    if (!email || !password) {
        showMessage('Please fill in all fields', 'error');
        return;
    }
    
    // Find user
    const user = users.find(u => 
        (u.email === email || u.phone === email) && u.password === password
    );
    
    if (user) {
        currentUser = user;
        localStorage.setItem('busbd_current_user', JSON.stringify(currentUser));
        showMessage('Login successful! Welcome back, ' + user.firstName, 'success');
        closeModal('loginModal');
        updateLoginStatus();
        document.getElementById('loginForm')?.reset();
    } else {
        showMessage('Invalid email/phone or password. Please try again.', 'error');
    }
}

function handleRegister(event) {
    event.preventDefault();
    console.log('Handling registration');
    
    const firstName = document.getElementById('firstName')?.value;
    const lastName = document.getElementById('lastName')?.value;
    const email = document.getElementById('registerEmail')?.value;
    const phone = document.getElementById('phone')?.value;
    const password = document.getElementById('registerPassword')?.value;
    const confirmPassword = document.getElementById('confirmPassword')?.value;
    const agreeTerms = document.getElementById('agreeTerms')?.checked;
    
    // Validation
    if (!firstName || !lastName || !email || !phone || !password || !confirmPassword) {
        showMessage('Please fill in all fields', 'error');
        return;
    }
    
    if (password !== confirmPassword) {
        showMessage('Passwords do not match!', 'error');
        return;
    }
    
    if (password.length < 6) {
        showMessage('Password must be at least 6 characters long!', 'error');
        return;
    }
    
    if (!agreeTerms) {
        showMessage('Please agree to the terms and conditions!', 'error');
        return;
    }
    
    // Check if user already exists
    const existingUser = users.find(u => u.email === email || u.phone === phone);
    if (existingUser) {
        showMessage('User with this email or phone already exists!', 'error');
        return;
    }
    
    // Create new user
    const newUser = {
        id: Date.now(),
        firstName,
        lastName,
        email,
        phone,
        password,
        registeredAt: new Date().toISOString()
    };
    
    users.push(newUser);
    localStorage.setItem('busbd_users', JSON.stringify(users));
    
    // Auto login
    currentUser = newUser;
    localStorage.setItem('busbd_current_user', JSON.stringify(currentUser));
    
    showMessage('Registration successful! Welcome to BusBD, ' + firstName, 'success');
    closeModal('registerModal');
    updateLoginStatus();
    document.getElementById('registerForm')?.reset();
}

// 3. BUS SEARCH FUNCTION
function searchBuses() {
    console.log('Searching buses');
    
    const from = document.getElementById('from')?.value;
    const to = document.getElementById('to')?.value;
    const date = document.getElementById('date')?.value;
    
    if (!from || !to || !date) {
        showMessage('Please fill in all search fields!', 'error');
        return;
    }
    
    if (from === to) {
        showMessage('Origin and destination cannot be the same!', 'error');
        return;
    }
    
    // Show loading
    const searchBtn = document.querySelector('.btn-search');
    if (searchBtn) {
        const originalText = searchBtn.innerHTML;
        searchBtn.innerHTML = 'Searching...';
        searchBtn.disabled = true;
        
        setTimeout(() => {
            searchBtn.innerHTML = originalText;
            searchBtn.disabled = false;
            showBusResults(from, to, date);
        }, 1500);
    }
}

// 4. BOOKING FUNCTION
function bookBus(busName, from, to, date, price) {
    console.log('Booking bus:', busName);
    
    if (!currentUser) {
        showMessage('Please login to book a ticket!', 'error');
        showLoginModal();
        return;
    }
    
    const bookingDetails = {
        busName,
        from,
        to,
        date,
        price,
        passenger: currentUser.firstName + ' ' + currentUser.lastName,
        bookingId: 'BUS' + Date.now()
    };
    
    showMessage(`Booking confirmed! Bus: ${busName} from ${from} to ${to} on ${date}. Booking ID: ${bookingDetails.bookingId}`, 'success');
    
    // Store booking
    const bookings = JSON.parse(localStorage.getItem('busbd_bookings')) || [];
    bookings.push(bookingDetails);
    localStorage.setItem('busbd_bookings', JSON.stringify(bookings));
}

// 5. UTILITY FUNCTIONS
function showMessage(message, type) {
    // Remove existing messages
    const existingMessages = document.querySelectorAll('.success-message, .error-message');
    existingMessages.forEach(msg => msg.remove());
    
    const messageDiv = document.createElement('div');
    messageDiv.className = type === 'success' ? 'success-message' : 'error-message';
    messageDiv.textContent = message;
    
    document.body.insertBefore(messageDiv, document.body.firstChild);
    
    setTimeout(() => {
        messageDiv.remove();
    }, 5000);
}

function updateLoginStatus() {
    const loginBtn = document.querySelector('.btn-login');
    const registerBtn = document.querySelector('.btn-register');
    
    if (loginBtn && registerBtn) {
        if (currentUser) {
            loginBtn.textContent = `Hi, ${currentUser.firstName}`;
            loginBtn.onclick = showUserMenu;
            registerBtn.style.display = 'none';
        } else {
            loginBtn.textContent = 'Login';
            loginBtn.onclick = showLoginModal;
            registerBtn.style.display = 'inline-block';
        }
    }
}

function showUserMenu() {
    const userMenu = confirm(`Hi ${currentUser.firstName}!\n\nChoose an option:\nOK - View Profile\nCancel - Logout`);
    
    if (userMenu) {
        alert('Profile page coming soon!');
    } else {
        currentUser = null;
        localStorage.removeItem('busbd_current_user');
        updateLoginStatus();
        showMessage('You have been logged out successfully!', 'success');
    }
}

function showBusResults(from, to, date) {
    const resultsSection = document.getElementById('bus-results');
    const busList = document.getElementById('buses-list');
    
    if (!resultsSection || !busList) return;
    
    // Clear previous results
    busList.innerHTML = '';
    
    // Sample bus data
    const buses = [
        {
            name: 'Green Line Paribahan',
            type: 'AC Business',
            departure: '08:00 AM',
            arrival: '02:30 PM',
            duration: '6h 30m',
            price: 800
        },
        {
            name: 'Shyamoli Paribahan',
            type: 'AC Business',
            departure: '09:30 AM',
            arrival: '04:00 PM',
            duration: '6h 30m',
            price: 750
        }
    ];
    
    buses.forEach(bus => {
        const busCard = document.createElement('div');
        busCard.className = 'bus-card';
        busCard.innerHTML = `
            <div class="bus-info">
                <h3>${bus.name}</h3>
                <p class="bus-type">${bus.type}</p>
            </div>
            <div class="route-info">
                <div class="time-info">
                    <div class="departure">${bus.departure}</div>
                    <div style="font-size: 0.9rem; color: #7F8C8D; margin: 0.5rem 0;">
                        ${from.charAt(0).toUpperCase() + from.slice(1)}
                    </div>
                </div>
                <div style="text-align: center; color: #7F8C8D;">
                    <i class="fas fa-arrow-right"></i>
                    <div class="duration">${bus.duration}</div>
                </div>
                <div class="time-info">
                    <div class="arrival">${bus.arrival}</div>
                    <div style="font-size: 0.9rem; color: #7F8C8D; margin: 0.5rem 0;">
                        ${to.charAt(0).toUpperCase() + to.slice(1)}
                    </div>
                </div>
            </div>
            <div class="price-info">
                <div class="price">৳${bus.price}</div>
                <div class="currency">per seat</div>
            </div>
            <button class="btn-book" onclick="bookBus('${bus.name}', '${from}', '${to}', '${date}', ${bus.price})">
                Book Now
            </button>
        `;
        busList.appendChild(busCard);
    });
    
    resultsSection.style.display = 'block';
    resultsSection.scrollIntoView({ behavior: 'smooth' });
}

// 6. INITIALIZATION
document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM loaded, initializing...');
    
    // Set minimum date to today
    const dateInput = document.getElementById('date');
    if (dateInput) {
        const today = new Date().toISOString().split('T')[0];
        dateInput.min = today;
        dateInput.value = today;
    }
    
    // Initialize login status
    updateLoginStatus();
    
    // Close modal when clicking outside
    window.onclick = function(event) {
        if (event.target.classList.contains('modal')) {
            const modalId = event.target.id;
            if (modalId) {
                closeModal(modalId);
            }
        }
    }
    
    console.log('Initialization complete. Functions available:', {
        showLoginModal: typeof showLoginModal,
        showRegisterModal: typeof showRegisterModal,
        closeModal: typeof closeModal,
        handleLogin: typeof handleLogin,
        handleRegister: typeof handleRegister,
        searchBuses: typeof searchBuses,
        bookBus: typeof bookBus
    });
});