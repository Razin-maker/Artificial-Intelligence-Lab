// Set minimum date to today
document.addEventListener('DOMContentLoaded', function() {
    const dateInput = document.getElementById('date');
    const today = new Date().toISOString().split('T')[0];
    dateInput.min = today;
    dateInput.value = today;
});

// Sample bus data for Bangladesh routes
const busData = {
    'dhaka-chittagong': [
        {
            name: 'Green Line Paribahan',
            type: 'AC Business',
            departure: '08:00 AM',
            arrival: '02:30 PM',
            duration: '6h 30m',
            price: 800,
            available: true
        },
        {
            name: 'Shyamoli Paribahan',
            type: 'AC Business',
            departure: '09:30 AM',
            arrival: '04:00 PM',
            duration: '6h 30m',
            price: 750,
            available: true
        },
        {
            name: 'Hanif Enterprise',
            type: 'AC Sleeper',
            departure: '10:00 PM',
            arrival: '05:30 AM',
            duration: '7h 30m',
            price: 1200,
            available: true
        }
    ],
    'dhaka-sylhet': [
        {
            name: 'Ena Transport',
            type: 'AC Business',
            departure: '07:00 AM',
            arrival: '01:00 PM',
            duration: '6h 00m',
            price: 650,
            available: true
        },
        {
            name: 'Shyamoli Paribahan',
            type: 'AC Business',
            departure: '08:30 AM',
            arrival: '02:30 PM',
            duration: '6h 00m',
            price: 600,
            available: true
        },
        {
            name: 'London Express',
            type: 'AC Sleeper',
            departure: '11:00 PM',
            arrival: '06:00 AM',
            duration: '7h 00m',
            price: 950,
            available: true
        }
    ],
    'dhaka-rajshahi': [
        {
            name: 'Royal Coach',
            type: 'AC Business',
            departure: '06:30 AM',
            arrival: '01:30 PM',
            duration: '7h 00m',
            price: 700,
            available: true
        },
        {
            name: 'TR Travels',
            type: 'AC Business',
            departure: '08:00 AM',
            arrival: '03:00 PM',
            duration: '7h 00m',
            price: 680,
            available: true
        }
    ],
    'chittagong-sylhet': [
        {
            name: 'Soudia Transport',
            type: 'AC Business',
            departure: '09:00 AM',
            arrival: '05:00 PM',
            duration: '8h 00m',
            price: 850,
            available: true
        },
        {
            name: 'Unique Service',
            type: 'Non-AC',
            departure: '10:30 AM',
            arrival: '07:30 PM',
            duration: '9h 00m',
            price: 550,
            available: true
        }
    ]
};

// User storage (in a real app, this would be a database)
let users = JSON.parse(localStorage.getItem('busbd_users')) || [];
let currentUser = JSON.parse(localStorage.getItem('busbd_current_user')) || null;

// Update UI based on login status
function updateLoginStatus() {
    const loginBtn = document.querySelector('.btn-login');
    const registerBtn = document.querySelector('.btn-register');
    
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

// Initialize login status on page load
updateLoginStatus();

// Modal functions
function showLoginModal() {
    document.getElementById('loginModal').style.display = 'block';
}

function showRegisterModal() {
    document.getElementById('registerModal').style.display = 'block';
}

function closeModal(modalId) {
    document.getElementById(modalId).style.display = 'none';
}

function switchToRegister() {
    closeModal('loginModal');
    showRegisterModal();
}

function switchToLogin() {
    closeModal('registerModal');
    showLoginModal();
}

// Close modal when clicking outside
window.onclick = function(event) {
    const loginModal = document.getElementById('loginModal');
    const registerModal = document.getElementById('registerModal');
    
    if (event.target === loginModal) {
        closeModal('loginModal');
    }
    if (event.target === registerModal) {
        closeModal('registerModal');
    }
}

// Login form handling
function handleLogin(event) {
    event.preventDefault();
    
    const email = document.getElementById('loginEmail').value;
    const password = document.getElementById('loginPassword').value;
    const rememberMe = document.getElementById('rememberMe').checked;
    
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
        
        // Clear form
        document.getElementById('loginForm').reset();
    } else {
        showMessage('Invalid email/phone or password. Please try again.', 'error');
    }
}

// Registration form handling
function handleRegister(event) {
    event.preventDefault();
    
    const firstName = document.getElementById('firstName').value;
    const lastName = document.getElementById('lastName').value;
    const email = document.getElementById('registerEmail').value;
    const phone = document.getElementById('phone').value;
    const password = document.getElementById('registerPassword').value;
    const confirmPassword = document.getElementById('confirmPassword').value;
    const agreeTerms = document.getElementById('agreeTerms').checked;
    
    // Validation
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
    
    // Clear form
    document.getElementById('registerForm').reset();
}

// Show message function
function showMessage(message, type) {
    // Remove existing messages
    const existingMessages = document.querySelectorAll('.success-message, .error-message');
    existingMessages.forEach(msg => msg.remove());
    
    const messageDiv = document.createElement('div');
    messageDiv.className = type === 'success' ? 'success-message' : 'error-message';
    messageDiv.textContent = message;
    
    // Insert at the top of the page
    document.body.insertBefore(messageDiv, document.body.firstChild);
    
    // Remove message after 5 seconds
    setTimeout(() => {
        messageDiv.remove();
    }, 5000);
}

// Bus search functionality
function searchBuses() {
    const from = document.getElementById('from').value;
    const to = document.getElementById('to').value;
    const date = document.getElementById('date').value;
    
    if (!from || !to || !date) {
        showMessage('Please fill in all search fields!', 'error');
        return;
    }
    
    if (from === to) {
        showMessage('Origin and destination cannot be the same!', 'error');
        return;
    }
    
    const routeKey = `${from}-${to}`;
    const reverseRouteKey = `${to}-${from}`;
    
    let buses = busData[routeKey] || busData[reverseRouteKey] || [];
    
    if (buses.length === 0) {
        buses = generateRandomBuses(from, to);
    }
    
    displayBusResults(buses, from, to, date);
}

// Generate random buses for routes not in sample data
function generateRandomBuses(from, to) {
    const busCompanies = [
        'Shyamoli Paribahan', 'Green Line', 'Hanif Enterprise', 
        'Ena Transport', 'Shohagh Paribahan', 'Royal Coach',
        'TR Travels', 'Soudia Transport', 'Unique Service'
    ];
    
    const busTypes = ['AC Business', 'AC Sleeper', 'Non-AC'];
    const buses = [];
    
    const numBuses = Math.floor(Math.random() * 4) + 2; // 2-5 buses
    
    for (let i = 0; i < numBuses; i++) {
        const departureHour = Math.floor(Math.random() * 16) + 6; // 6 AM to 10 PM
        const departureMin = Math.random() < 0.5 ? '00' : '30';
        const departure = `${departureHour.toString().padStart(2, '0')}:${departureMin} ${departureHour < 12 ? 'AM' : 'PM'}`;
        
        const travelTime = Math.floor(Math.random() * 4) + 4; // 4-7 hours
        const arrivalHour = (departureHour + travelTime) % 24;
        const arrival = `${arrivalHour.toString().padStart(2, '0')}:${departureMin} ${arrivalHour < 12 ? 'AM' : 'PM'}`;
        
        const busType = busTypes[Math.floor(Math.random() * busTypes.length)];
        let basePrice = 500;
        if (busType === 'AC Business') basePrice = 700;
        if (busType === 'AC Sleeper') basePrice = 1000;
        
        buses.push({
            name: busCompanies[Math.floor(Math.random() * busCompanies.length)],
            type: busType,
            departure: departure,
            arrival: arrival,
            duration: `${travelTime}h 00m`,
            price: basePrice + Math.floor(Math.random() * 300),
            available: true
        });
    }
    
    return buses;
}

// Display bus search results
function displayBusResults(buses, from, to, date) {
    const resultsSection = document.getElementById('bus-results');
    const busList = document.getElementById('buses-list');
    
    // Clear previous results
    busList.innerHTML = '';
    
    if (buses.length === 0) {
        busList.innerHTML = '<p style="text-align: center; color: #7F8C8D; font-size: 1.2rem;">No buses found for this route. Please try different cities.</p>';
    } else {
        buses.forEach(bus => {
            const busCard = createBusCard(bus, from, to, date);
            busList.appendChild(busCard);
        });
    }
    
    // Show results section and scroll to it
    resultsSection.style.display = 'block';
    resultsSection.scrollIntoView({ behavior: 'smooth' });
}

// Create bus card element
function createBusCard(bus, from, to, date) {
    const card = document.createElement('div');
    card.className = 'bus-card';
    
    const fromCity = capitalizeFirst(from);
    const toCity = capitalizeFirst(to);
    
    card.innerHTML = `
        <div class="bus-info">
            <h3>${bus.name}</h3>
            <p class="bus-type">${bus.type}</p>
        </div>
        <div class="route-info">
            <div class="time-info">
                <div class="departure">${bus.departure}</div>
                <div style="font-size: 0.9rem; color: #7F8C8D; margin: 0.5rem 0;">
                    ${fromCity}
                </div>
            </div>
            <div style="text-align: center; color: #7F8C8D;">
                <i class="fas fa-arrow-right"></i>
                <div class="duration">${bus.duration}</div>
            </div>
            <div class="time-info">
                <div class="arrival">${bus.arrival}</div>
                <div style="font-size: 0.9rem; color: #7F8C8D; margin: 0.5rem 0;">
                    ${toCity}
                </div>
            </div>
        </div>
        <div class="price-info">
            <div class="price">৳${bus.price}</div>
            <div class="currency">per seat</div>
        </div>
        <button class="btn-book" onclick="bookBus('${bus.name}', '${fromCity}', '${toCity}', '${date}', ${bus.price})">
            Book Now
        </button>
    `;
    
    return card;
}

// Capitalize first letter
function capitalizeFirst(str) {
    return str.charAt(0).toUpperCase() + str.slice(1);
}

// Book bus function
function bookBus(busName, from, to, date, price) {
    if (!currentUser) {
        showMessage('Please login to book a ticket!', 'error');
        showLoginModal();
        return;
    }
    
    // In a real application, this would redirect to a booking page
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
    
    // Store booking (in real app, this would go to a server)
    const bookings = JSON.parse(localStorage.getItem('busbd_bookings')) || [];
    bookings.push(bookingDetails);
    localStorage.setItem('busbd_bookings', JSON.stringify(bookings));
}

// User menu function (placeholder)
function showUserMenu() {
    const userMenu = confirm(`Hi ${currentUser.firstName}!\n\nChoose an option:\nOK - View Profile\nCancel - Logout`);
    
    if (userMenu) {
        // Show user profile (placeholder)
        alert('Profile page coming soon!');
    } else {
        // Logout
        currentUser = null;
        localStorage.removeItem('busbd_current_user');
        updateLoginStatus();
        showMessage('You have been logged out successfully!', 'success');
    }
}

// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Mobile navigation toggle
const hamburger = document.querySelector('.hamburger');
const navMenu = document.querySelector('.nav-menu');

if (hamburger) {
    hamburger.addEventListener('click', () => {
        hamburger.classList.toggle('active');
        navMenu.classList.toggle('active');
    });
}

// Contact form handling
document.querySelector('.contact-form form').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const name = this.querySelector('input[type="text"]').value;
    const email = this.querySelector('input[type="email"]').value;
    const message = this.querySelector('textarea').value;
    
    if (name && email && message) {
        showMessage('Thank you for your message! We will get back to you soon.', 'success');
        this.reset();
    } else {
        showMessage('Please fill in all fields!', 'error');
    }
});

// Add loading state to search button
function addLoadingState() {
    const searchBtn = document.querySelector('.btn-search');
    const originalText = searchBtn.innerHTML;
    
    searchBtn.innerHTML = '<div class="loading"></div> Searching...';
    searchBtn.disabled = true;
    
    setTimeout(() => {
        searchBtn.innerHTML = originalText;
        searchBtn.disabled = false;
    }, 1000);
}

// Override search function to include loading
const originalSearchBuses = searchBuses;
searchBuses = function() {
    addLoadingState();
    setTimeout(originalSearchBuses, 1000);
};