# BusBD Demo Guide

## How to Test the Website

### 1. Open the Website
Simply open `index.html` in any modern web browser (Chrome, Firefox, Safari, Edge).

### 2. Test User Registration
1. Click the "Register" button in the navigation
2. Fill in the registration form:
   - **First Name**: Rafiq
   - **Last Name**: Ahmed
   - **Email**: rafiq.ahmed@email.com
   - **Phone**: +880 1711-123456
   - **Password**: 123456
   - **Confirm Password**: 123456
   - ✓ Check "I agree to the Terms and Conditions"
3. Click "Create Account"
4. You should see a success message and be automatically logged in

### 3. Test Bus Search
1. In the booking form on the hero section:
   - **From**: Select "Dhaka"
   - **To**: Select "Chittagong"
   - **Date**: Choose today's date or any future date
2. Click "Search Buses"
3. Wait for the loading animation
4. Scroll down to see available buses

### 4. Test Booking
1. After searching for buses, you'll see a list of available buses
2. Click "Book Now" on any bus
3. Since you're logged in, you'll get a booking confirmation
4. Note the booking ID for reference

### 5. Test Login/Logout
1. Click on your name in the navigation (top right)
2. Choose "Cancel" to logout
3. Click "Login" button
4. Use the credentials you registered with:
   - **Email or Phone**: rafiq.ahmed@email.com or +880 1711-123456
   - **Password**: 123456
5. Check "Remember me" if desired
6. Click "Login"

### 6. Test Different Routes
Try searching for these popular routes:
- **Dhaka to Sylhet**
- **Dhaka to Rajshahi**
- **Chittagong to Sylhet**
- **Sylhet to Khulna** (will generate random buses)

### 7. Test Mobile Responsiveness
1. Open browser developer tools (F12)
2. Switch to mobile view (phone icon)
3. Test navigation, forms, and booking flow on mobile

### 8. Test Form Validations
Try these scenarios to test validation:
- Register with mismatched passwords
- Register with existing email/phone
- Login with wrong credentials
- Search buses without selecting cities
- Search with same origin and destination

### 9. Test Contact Form
1. Scroll down to the Contact section
2. Fill in the contact form:
   - **Name**: Your name
   - **Email**: Your email
   - **Message**: Test message
3. Click "Send Message"
4. You should see a success confirmation

### 10. Test Navigation
- Click on navigation links (Home, Services, About, Contact)
- Notice smooth scrolling to sections
- Test on mobile with hamburger menu

## Sample Test Data

### Popular Routes with Pre-loaded Data:
- **Dhaka ↔ Chittagong**
- **Dhaka ↔ Sylhet**
- **Dhaka ↔ Rajshahi**
- **Chittagong ↔ Sylhet**

### Bus Companies You'll See:
- Green Line Paribahan
- Shyamoli Paribahan
- Hanif Enterprise
- Ena Transport
- London Express
- Royal Coach

### Expected Pricing:
- **Non-AC**: ৳500-800
- **AC Business**: ৳600-900
- **AC Sleeper**: ৳950-1200

## Features to Notice

### Design Elements:
- ✅ Bangladesh flag colors (green and red)
- ✅ Beautiful animations (floating bus icon)
- ✅ Smooth transitions and hover effects
- ✅ Professional typography and spacing
- ✅ Mobile-first responsive design

### User Experience:
- ✅ Instant feedback on all actions
- ✅ Loading states for better UX
- ✅ Clear error and success messages
- ✅ Intuitive navigation flow
- ✅ Bangladesh context throughout

### Technical Features:
- ✅ Form validation
- ✅ Local storage persistence
- ✅ Dynamic content generation
- ✅ Modal management
- ✅ Responsive layouts

## Expected Behavior

1. **Registration**: Creates account and auto-logs in
2. **Login**: Remembers session across page reloads
3. **Search**: Shows buses with realistic timing and pricing
4. **Booking**: Requires login, stores booking in local storage
5. **Responsive**: Works perfectly on all screen sizes
6. **Validation**: Prevents invalid actions with helpful messages

## Local Storage Data

The website stores data in your browser's local storage:
- `busbd_users`: Array of registered users
- `busbd_current_user`: Currently logged-in user
- `busbd_bookings`: User's booking history

You can view this data in browser developer tools > Application > Local Storage.

---

**Enjoy testing the BusBD bus ticketing website!** 🚌🇧🇩