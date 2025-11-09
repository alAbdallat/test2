import os
from flask import Flask, render_template, request, redirect, url_for

# Initialize the Flask application
# The use of __name__ is standard practice
app = Flask(__name__)

# --- In-Memory Data Storage (Placeholder for Database) ---
# We will temporarily store successful bookings in this list.
bookings = []

# --- ROUTE 1: Home/Service Selection Page ---
# This is the entry point (homepage) of the application.
@app.route('/')
def index():
    # render_template looks for 'index.html' inside a 'templates' folder.
    return render_template('index.html')

# --- ROUTE 2: Handle Booking Submission ---
# This route handles the POST request when the user submits the form.
@app.route('/book', methods=['POST'])
def book():
    # We use request.form to get data sent via the HTML form
    user_name = request.form.get('name')
    service = request.form.get('service')
    location = request.form.get('location')
    
    # Check if we got the necessary data
    if user_name and service and location:
        # Create a booking record
        new_booking = {
            "id": len(bookings) + 1,
            "name": user_name,
            "service": service,
            "location": location,
            "status": "Pending"
        }
        
        # Save the record to our temporary list
        bookings.append(new_booking)
        
        # --- Crucial for debugging and practicability ---
        # Print the data to the console (our "database" check)
        print(f"--- NEW BOOKING RECEIVED ---")
        print(f"ID: {new_booking['id']}")
        print(f"Customer: {new_booking['name']}")
        print(f"Service: {new_booking['service']}")
        print(f"Location: {new_booking['location']}")
        print(f"All Bookings: {bookings}")
        print(f"------------------------------------")
        
        # Redirect the user to a success page
        # Note: We use url_for to dynamically generate the URL for the 'success' function.
        return redirect(url_for('success'))
    
    # If data is missing, redirect back to the home page (you could also show an error message)
    return redirect(url_for('index'))

# --- ROUTE 3: Success Confirmation Page ---
@app.route('/success')
def success():
    # Simple success page, we could make this look nicer later.
    return "<h1>Booking Confirmed!</h1><p>Thank you for your request. We have logged your service request.</p><p><a href='/'>Go Home</a></p>"

# --- Application Startup ---
if __name__ == '__main__':
    # When running locally, Flask uses this block.
    # debug=True allows the server to auto-reload when you save changes.
    # It should be FALSE in a production/live environment.
    app.run(debug=True)
    
