import tkinter as tk
from tkinter import messagebox
from datetime import datetime

from services import UserService, CarService, BookingService


class CarRentalApp:
    """Main graphical interface for the Car Rental System."""

    def __init__(self, root):
        self.root = root
        self.root.title("Car Rental System")
        self.root.geometry("650x750")

        self.user_service = UserService()
        self.current_user = None

        self.create_login_screen()

    def clear_window(self):
        """Remove all widgets from the current window."""
        for widget in self.root.winfo_children():
            widget.destroy()

    # =========================================================
    # LOGIN
    # =========================================================

    def create_login_screen(self):
        """Create the login screen."""

        self.clear_window()

        tk.Label(
            self.root,
            text="CAR RENTAL SYSTEM",
            font=("Arial", 20, "bold")
        ).pack(pady=30)

        tk.Label(self.root, text="Username:").pack()

        self.username_entry = tk.Entry(
            self.root,
            width=30
        )
        self.username_entry.pack(pady=5)

        tk.Label(self.root, text="Password:").pack()

        self.password_entry = tk.Entry(
            self.root,
            width=30,
            show="*"
        )
        self.password_entry.pack(pady=5)

        tk.Button(
            self.root,
            text="Login",
            width=20,
            command=self.login
        ).pack(pady=15)

        tk.Button(
            self.root,
            text="Register",
            width=20,
            command=self.create_register_screen
        ).pack()

    def login(self):
        """Log the user into the system."""

        username = self.username_entry.get().strip()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showwarning(
                "Missing Information",
                "Please enter your username and password."
            )
            return

        user = self.user_service.login_user(
            username,
            password
        )

        if user is None:
            messagebox.showerror(
                "Login Failed",
                "Incorrect username or password."
            )
            return

        self.current_user = user

        if user.role == "admin":
            self.create_admin_dashboard(user)
        else:
            self.create_customer_dashboard(user)

    # =========================================================
    # REGISTRATION
    # =========================================================

    def create_register_screen(self):
        """Create customer registration screen."""

        self.clear_window()

        tk.Label(
            self.root,
            text="CUSTOMER REGISTRATION",
            font=("Arial", 18, "bold")
        ).pack(pady=25)

        tk.Label(self.root, text="Username:").pack()

        self.register_username_entry = tk.Entry(
            self.root,
            width=30
        )
        self.register_username_entry.pack(pady=5)

        tk.Label(self.root, text="Password:").pack()

        self.register_password_entry = tk.Entry(
            self.root,
            width=30,
            show="*"
        )
        self.register_password_entry.pack(pady=5)

        tk.Label(
            self.root,
            text="Confirm Password:"
        ).pack()

        self.confirm_password_entry = tk.Entry(
            self.root,
            width=30,
            show="*"
        )
        self.confirm_password_entry.pack(pady=5)

        tk.Button(
            self.root,
            text="Create Account",
            width=20,
            command=self.register
        ).pack(pady=15)

        tk.Button(
            self.root,
            text="Back to Login",
            width=20,
            command=self.create_login_screen
        ).pack()

    def register(self):
        """Register a new customer."""

        username = self.register_username_entry.get().strip()
        password = self.register_password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if not username or not password:
            messagebox.showwarning(
                "Missing Information",
                "Please complete all fields."
            )
            return

        if password != confirm_password:
            messagebox.showerror(
                "Registration Failed",
                "Passwords do not match."
            )
            return

        success, message = self.user_service.register_user(
            username,
            password,
            "customer"
        )

        if success:
            messagebox.showinfo(
                "Registration Successful",
                "Your account has been created."
            )
            self.create_login_screen()
        else:
            messagebox.showerror(
                "Registration Failed",
                message
            )

    # =========================================================
    # CUSTOMER DASHBOARD
    # =========================================================

    def create_customer_dashboard(self, user):
        """Display the customer dashboard."""

        self.clear_window()

        tk.Label(
            self.root,
            text="CUSTOMER DASHBOARD",
            font=("Arial", 20, "bold")
        ).pack(pady=30)

        tk.Label(
            self.root,
            text=f"Welcome, {user.username}!"
        ).pack(pady=10)

        tk.Button(
            self.root,
            text="View Available Cars",
            width=25,
            command=self.view_available_cars
        ).pack(pady=10)

        tk.Button(
            self.root,
            text="My Bookings",
            width=25,
            command=self.view_my_bookings
        ).pack(pady=10)

        tk.Button(
            self.root,
            text="Logout",
            width=25,
            command=self.logout
        ).pack(pady=20)

    # =========================================================
    # VIEW AVAILABLE CARS
    # =========================================================

    def view_available_cars(self):
        """Display all currently available cars."""

        car_service = CarService()
        cars = car_service.get_available_cars()

        self.clear_window()

        tk.Label(
            self.root,
            text="AVAILABLE CARS",
            font=("Arial", 20, "bold")
        ).pack(pady=20)

        if not cars:
            tk.Label(
                self.root,
                text="No cars are currently available."
            ).pack(pady=20)

        else:
            for car in cars:

                (
                    car_id,
                    make,
                    model,
                    year,
                    mileage,
                    available,
                    min_period,
                    max_period,
                    daily_rate
                ) = car

                car_frame = tk.Frame(
                    self.root,
                    relief="solid",
                    borderwidth=1
                )

                car_frame.pack(
                    fill="x",
                    padx=20,
                    pady=5
                )

                car_text = (
                    f"{make} {model} ({year})\n"
                    f"Mileage: {mileage} km\n"
                    f"Daily Rate: ${daily_rate:.2f}\n"
                    f"Rental Period: "
                    f"{min_period}-{max_period} days\n"
                    f"Status: Available"
                )

                tk.Label(
                    car_frame,
                    text=car_text,
                    justify="left",
                    padx=10,
                    pady=10
                ).pack(side="left")

                tk.Button(
                    car_frame,
                    text="Book This Car",
                    command=lambda car=car:
                    self.create_booking_screen(car)
                ).pack(
                    side="right",
                    padx=10
                )

        tk.Button(
            self.root,
            text="Back to Dashboard",
            width=25,
            command=lambda:
            self.create_customer_dashboard(
                self.current_user
            )
        ).pack(pady=20)

        car_service.close()

    # =========================================================
    # BOOKING SCREEN
    # =========================================================

    def create_booking_screen(self, car):
        """Create the rental booking form."""

        self.clear_window()

        self.selected_car = car

        (
            car_id,
            make,
            model,
            year,
            mileage,
            available,
            min_period,
            max_period,
            daily_rate
        ) = car

        tk.Label(
            self.root,
            text="RENTAL BOOKING",
            font=("Arial", 20, "bold")
        ).pack(pady=20)

        tk.Label(
            self.root,
            text=f"{make} {model} ({year})",
            font=("Arial", 15, "bold")
        ).pack()

        tk.Label(
            self.root,
            text=f"Daily Rate: ${daily_rate:.2f}"
        ).pack()

        tk.Label(
            self.root,
            text=f"Rental Period: "
                 f"{min_period}-{max_period} days"
        ).pack(pady=5)

        tk.Label(
            self.root,
            text="Start Date (DD/MM/YYYY):"
        ).pack(pady=(20, 5))

        self.start_date_entry = tk.Entry(
            self.root,
            width=30
        )
        self.start_date_entry.pack()

        tk.Label(
            self.root,
            text="End Date (DD/MM/YYYY):"
        ).pack(pady=(10, 5))

        self.end_date_entry = tk.Entry(
            self.root,
            width=30
        )
        self.end_date_entry.pack()

        tk.Label(
            self.root,
            text="Additional Charges ($):"
        ).pack(pady=(10, 5))

        self.additional_charge_entry = tk.Entry(
            self.root,
            width=30
        )
        self.additional_charge_entry.insert(0, "0")
        self.additional_charge_entry.pack()

        tk.Button(
            self.root,
            text="Calculate Fee",
            width=20,
            command=self.calculate_booking_fee
        ).pack(pady=15)

        self.fee_label = tk.Label(
            self.root,
            text=""
        )
        self.fee_label.pack(pady=5)

        tk.Button(
            self.root,
            text="Confirm Booking",
            width=20,
            command=self.confirm_booking
        ).pack(pady=10)

        tk.Button(
            self.root,
            text="Back to Available Cars",
            width=25,
            command=self.view_available_cars
        ).pack(pady=10)

    # =========================================================
    # CALCULATE FEE
    # =========================================================

    def calculate_booking_fee(self):
        """Calculate the total rental fee."""

        start_date_text = self.start_date_entry.get().strip()
        end_date_text = self.end_date_entry.get().strip()
        additional_charge_text = (
            self.additional_charge_entry.get().strip()
        )

        try:
            start_date = datetime.strptime(
                start_date_text,
                "%d/%m/%Y"
            )

            end_date = datetime.strptime(
                end_date_text,
                "%d/%m/%Y"
            )

            additional_charge = float(
                additional_charge_text
            )

        except ValueError:
            messagebox.showerror(
                "Invalid Information",
                "Please enter valid dates and charges."
            )
            return

        if end_date <= start_date:
            messagebox.showerror(
                "Invalid Dates",
                "End date must be after start date."
            )
            return

        if additional_charge < 0:
            messagebox.showerror(
                "Invalid Charge",
                "Additional charges cannot be negative."
            )
            return

        rental_days = (
            end_date - start_date
        ).days

        (
            car_id,
            make,
            model,
            year,
            mileage,
            available,
            min_period,
            max_period,
            daily_rate
        ) = self.selected_car

        if rental_days < min_period:
            messagebox.showerror(
                "Rental Period Too Short",
                f"Minimum rental period is "
                f"{min_period} days."
            )
            return

        if rental_days > max_period:
            messagebox.showerror(
                "Rental Period Too Long",
                f"Maximum rental period is "
                f"{max_period} days."
            )
            return

        rental_fee = rental_days * daily_rate
        total_fee = rental_fee + additional_charge

        self.calculated_total = total_fee

        self.fee_label.config(
            text=(
                f"Rental Days: {rental_days}\n"
                f"Rental Fee: ${rental_fee:.2f}\n"
                f"Additional Charges: "
                f"${additional_charge:.2f}\n"
                f"TOTAL FEE: ${total_fee:.2f}"
            )
        )

    # =========================================================
    # CONFIRM BOOKING
    # =========================================================

    def confirm_booking(self):
        """Save the customer's booking."""

        if not hasattr(self, "calculated_total"):
            messagebox.showwarning(
                "Calculate Fee First",
                "Please calculate the rental fee first."
            )
            return

        start_date = self.start_date_entry.get().strip()
        end_date = self.end_date_entry.get().strip()

        car_id = self.selected_car[0]

        booking_service = BookingService()

        booking_service.create_booking(
            self.current_user.user_id,
            car_id,
            start_date,
            end_date,
            self.calculated_total
        )

        booking_service.close()

        messagebox.showinfo(
            "Booking Successful",
            "Your booking has been submitted.\n\n"
            "Status: Pending\n\n"
            "An admin must approve the booking."
        )

        self.create_customer_dashboard(
            self.current_user
        )

    # =========================================================
    # CUSTOMER BOOKINGS
    # =========================================================

    def view_my_bookings(self):
        """Display the customer's bookings."""

        booking_service = BookingService()

        bookings = booking_service.get_customer_bookings(
            self.current_user.user_id
        )

        self.clear_window()

        tk.Label(
            self.root,
            text="MY BOOKINGS",
            font=("Arial", 20, "bold")
        ).pack(pady=20)

        if not bookings:

            tk.Label(
                self.root,
                text="You have no bookings."
            ).pack(pady=20)

        else:

            for booking in bookings:

                (
                    booking_id,
                    make,
                    model,
                    start_date,
                    end_date,
                    total_fee,
                    status
                ) = booking

                booking_text = (
                    f"Booking ID: {booking_id}\n"
                    f"Car: {make} {model}\n"
                    f"Start Date: {start_date}\n"
                    f"End Date: {end_date}\n"
                    f"Total Fee: ${total_fee:.2f}\n"
                    f"Status: {status}"
                )

                tk.Label(
                    self.root,
                    text=booking_text,
                    justify="left",
                    relief="solid",
                    padx=10,
                    pady=10
                ).pack(
                    fill="x",
                    padx=30,
                    pady=5
                )

        tk.Button(
            self.root,
            text="Back to Dashboard",
            width=25,
            command=lambda:
            self.create_customer_dashboard(
                self.current_user
            )
        ).pack(pady=20)

        booking_service.close()

    # =========================================================
    # ADMIN DASHBOARD
    # =========================================================

    def create_admin_dashboard(self, user):
        """Display the admin dashboard."""

        self.clear_window()

        tk.Label(
            self.root,
            text="ADMIN DASHBOARD",
            font=("Arial", 20, "bold")
        ).pack(pady=30)

        tk.Label(
            self.root,
            text=f"Welcome, {user.username}!"
        ).pack(pady=10)

        tk.Button(
            self.root,
            text="Manage Cars",
            width=25,
            command=self.manage_cars
        ).pack(pady=10)

        tk.Button(
            self.root,
            text="Manage Bookings",
            width=25,
            command=self.manage_bookings
        ).pack(pady=10)

        tk.Button(
            self.root,
            text="Logout",
            width=25,
            command=self.logout
        ).pack(pady=20)

    # =========================================================
    # ADMIN MANAGE BOOKINGS
    # =========================================================

    def manage_bookings(self):
        """Display all customer bookings to the admin."""

        booking_service = BookingService()

        bookings = booking_service.get_all_bookings()

        self.clear_window()

        tk.Label(
            self.root,
            text="MANAGE BOOKINGS",
            font=("Arial", 20, "bold")
        ).pack(pady=20)

        if not bookings:

            tk.Label(
                self.root,
                text="No bookings found."
            ).pack(pady=20)

        else:

            for booking in bookings:

                (
                    booking_id,
                    username,
                    make,
                    model,
                    start_date,
                    end_date,
                    total_fee,
                    status
                ) = booking

                booking_frame = tk.Frame(
                    self.root,
                    relief="solid",
                    borderwidth=1
                )

                booking_frame.pack(
                    fill="x",
                    padx=20,
                    pady=8
                )

                booking_text = (
                    f"Booking ID: {booking_id}\n"
                    f"Customer: {username}\n"
                    f"Car: {make} {model}\n"
                    f"Start Date: {start_date}\n"
                    f"End Date: {end_date}\n"
                    f"Total Fee: ${total_fee:.2f}\n"
                    f"Status: {status}"
                )

                tk.Label(
                    booking_frame,
                    text=booking_text,
                    justify="left",
                    padx=10,
                    pady=10
                ).pack(side="left")

                if status == "Pending":

                    button_frame = tk.Frame(
                        booking_frame
                    )

                    button_frame.pack(
                        side="right",
                        padx=10
                    )

                    tk.Button(
                        button_frame,
                        text="Approve",
                        command=lambda booking_id=booking_id:
                        self.update_booking_status(
                            booking_id,
                            "Approved"
                        )
                    ).pack(pady=3)

                    tk.Button(
                        button_frame,
                        text="Reject",
                        command=lambda booking_id=booking_id:
                        self.update_booking_status(
                            booking_id,
                            "Rejected"
                        )
                    ).pack(pady=3)

        tk.Button(
            self.root,
            text="Back to Admin Dashboard",
            width=25,
            command=lambda:
            self.create_admin_dashboard(
                self.current_user
            )
        ).pack(pady=20)

        booking_service.close()

    # =========================================================
    # UPDATE BOOKING STATUS
    # =========================================================

    def update_booking_status(
        self,
        booking_id,
        status
    ):
        """Approve or reject a customer booking."""

        booking_service = BookingService()

        booking_service.update_booking_status(
            booking_id,
            status
        )

        booking_service.close()

        messagebox.showinfo(
            "Booking Updated",
            f"Booking #{booking_id} is now "
            f"{status}."
        )

        self.manage_bookings()

    # =========================================================
    # ADMIN MANAGE CARS
    # =========================================================

    def manage_cars(self):
        """Display all cars and management options."""

        car_service = CarService()
        cars = car_service.get_all_cars()

        self.clear_window()

        tk.Label(
            self.root,
            text="MANAGE CARS",
            font=("Arial", 20, "bold")
        ).pack(pady=20)

        if not cars:

            tk.Label(
                self.root,
                text="No cars found."
            ).pack(pady=20)

        else:

            for car in cars:

                (
                    car_id,
                    make,
                    model,
                    year,
                    mileage,
                    available,
                    min_period,
                    max_period,
                    daily_rate
                ) = car

                status = (
                    "Available"
                    if available
                    else "Not Available"
                )

                car_frame = tk.Frame(
                    self.root,
                    relief="solid",
                    borderwidth=1
                )

                car_frame.pack(
                    fill="x",
                    padx=20,
                    pady=5
                )

                car_text = (
                    f"ID: {car_id}\n"
                    f"{make} {model} ({year})\n"
                    f"Mileage: {mileage} km\n"
                    f"Daily Rate: ${daily_rate:.2f}\n"
                    f"Rental Period: "
                    f"{min_period}-{max_period} days\n"
                    f"Status: {status}"
                )

                tk.Label(
                    car_frame,
                    text=car_text,
                    justify="left",
                    padx=10,
                    pady=10
                ).pack(side="left")

                button_frame = tk.Frame(car_frame)
                button_frame.pack(
                    side="right",
                    padx=10
                )

                tk.Button(
                    button_frame,
                    text="Update",
                    command=lambda car=car:
                    self.create_update_car_screen(car)
                ).pack(pady=3)

                tk.Button(
                    button_frame,
                    text="Delete",
                    command=lambda car_id=car_id,
                    make=make,
                    model=model:
                    self.delete_car(
                        car_id,
                        make,
                        model
                    )
                ).pack(pady=3)

        tk.Button(
            self.root,
            text="Add New Car",
            width=25,
            command=self.create_add_car_screen
        ).pack(pady=10)

        tk.Button(
            self.root,
            text="Back to Admin Dashboard",
            width=25,
            command=self.back_to_admin_dashboard
        ).pack(pady=10)

        car_service.close()

    # =========================================================
    # DELETE CAR
    # =========================================================

    def delete_car(self, car_id, make, model):
        """Delete a car after confirmation."""

        answer = messagebox.askyesno(
            "Confirm Delete",
            f"Are you sure you want to delete "
            f"{make} {model}?"
        )

        if not answer:
            return

        car_service = CarService()

        car_service.delete_car(car_id)

        car_service.close()

        messagebox.showinfo(
            "Success",
            f"{make} {model} has been deleted."
        )

        self.manage_cars()

    # =========================================================
    # ADD CAR
    # =========================================================

    def create_add_car_screen(self):
        """Create the add-car form."""

        self.clear_window()

        tk.Label(
            self.root,
            text="ADD NEW CAR",
            font=("Arial", 20, "bold")
        ).pack(pady=15)

        tk.Label(self.root, text="Make:").pack()
        self.make_entry = tk.Entry(
            self.root,
            width=30
        )
        self.make_entry.pack(pady=3)

        tk.Label(self.root, text="Model:").pack()
        self.model_entry = tk.Entry(
            self.root,
            width=30
        )
        self.model_entry.pack(pady=3)

        tk.Label(self.root, text="Year:").pack()
        self.year_entry = tk.Entry(
            self.root,
            width=30
        )
        self.year_entry.pack(pady=3)

        tk.Label(self.root, text="Mileage:").pack()
        self.mileage_entry = tk.Entry(
            self.root,
            width=30
        )
        self.mileage_entry.pack(pady=3)

        tk.Label(
            self.root,
            text="Minimum Rental Period (days):"
        ).pack()

        self.min_period_entry = tk.Entry(
            self.root,
            width=30
        )
        self.min_period_entry.pack(pady=3)

        tk.Label(
            self.root,
            text="Maximum Rental Period (days):"
        ).pack()

        self.max_period_entry = tk.Entry(
            self.root,
            width=30
        )
        self.max_period_entry.pack(pady=3)

        tk.Label(
            self.root,
            text="Daily Rental Rate ($):"
        ).pack()

        self.daily_rate_entry = tk.Entry(
            self.root,
            width=30
        )
        self.daily_rate_entry.pack(pady=3)

        tk.Button(
            self.root,
            text="Add Car",
            width=20,
            command=self.add_car
        ).pack(pady=10)

        tk.Button(
            self.root,
            text="Back to Manage Cars",
            width=20,
            command=self.manage_cars
        ).pack()

    def add_car(self):
        """Validate and add a new car."""

        make = self.make_entry.get().strip()
        model = self.model_entry.get().strip()
        year = self.year_entry.get().strip()
        mileage = self.mileage_entry.get().strip()
        min_period = self.min_period_entry.get().strip()
        max_period = self.max_period_entry.get().strip()
        daily_rate = self.daily_rate_entry.get().strip()

        if not all([
            make,
            model,
            year,
            mileage,
            min_period,
            max_period,
            daily_rate
        ]):
            messagebox.showwarning(
                "Missing Information",
                "Please complete all fields."
            )
            return

        try:
            year = int(year)
            mileage = int(mileage)
            min_period = int(min_period)
            max_period = int(max_period)
            daily_rate = float(daily_rate)

        except ValueError:
            messagebox.showerror(
                "Invalid Information",
                "Please enter valid numbers."
            )
            return

        if min_period > max_period:
            messagebox.showerror(
                "Invalid Rental Period",
                "Minimum rental period cannot be greater "
                "than maximum rental period."
            )
            return

        if daily_rate <= 0:
            messagebox.showerror(
                "Invalid Daily Rate",
                "Daily rate must be greater than zero."
            )
            return

        car_service = CarService()

        car_service.add_car(
            make,
            model,
            year,
            mileage,
            min_period,
            max_period,
            daily_rate
        )

        car_service.close()

        messagebox.showinfo(
            "Success",
            "Car added successfully!"
        )

        self.manage_cars()

    # =========================================================
    # UPDATE CAR
    # =========================================================

    def create_update_car_screen(self, car):
        """Create the update-car form."""

        self.clear_window()

        (
            car_id,
            make,
            model,
            year,
            mileage,
            available,
            min_period,
            max_period,
            daily_rate
        ) = car

        tk.Label(
            self.root,
            text="UPDATE CAR",
            font=("Arial", 20, "bold")
        ).pack(pady=15)

        tk.Label(self.root, text="Make:").pack()

        self.update_make_entry = tk.Entry(
            self.root,
            width=30
        )
        self.update_make_entry.insert(0, make)
        self.update_make_entry.pack(pady=3)

        tk.Label(self.root, text="Model:").pack()

        self.update_model_entry = tk.Entry(
            self.root,
            width=30
        )
        self.update_model_entry.insert(0, model)
        self.update_model_entry.pack(pady=3)

        tk.Label(self.root, text="Year:").pack()

        self.update_year_entry = tk.Entry(
            self.root,
            width=30
        )
        self.update_year_entry.insert(0, year)
        self.update_year_entry.pack(pady=3)

        tk.Label(self.root, text="Mileage:").pack()

        self.update_mileage_entry = tk.Entry(
            self.root,
            width=30
        )
        self.update_mileage_entry.insert(0, mileage)
        self.update_mileage_entry.pack(pady=3)

        tk.Label(
            self.root,
            text="Minimum Rental Period (days):"
        ).pack()

        self.update_min_period_entry = tk.Entry(
            self.root,
            width=30
        )
        self.update_min_period_entry.insert(
            0,
            min_period
        )
        self.update_min_period_entry.pack(pady=3)

        tk.Label(
            self.root,
            text="Maximum Rental Period (days):"
        ).pack()

        self.update_max_period_entry = tk.Entry(
            self.root,
            width=30
        )
        self.update_max_period_entry.insert(
            0,
            max_period
        )
        self.update_max_period_entry.pack(pady=3)

        tk.Label(
            self.root,
            text="Daily Rental Rate ($):"
        ).pack()

        self.update_daily_rate_entry = tk.Entry(
            self.root,
            width=30
        )
        self.update_daily_rate_entry.insert(
            0,
            daily_rate
        )
        self.update_daily_rate_entry.pack(pady=3)

        tk.Button(
            self.root,
            text="Update Car",
            width=20,
            command=lambda:
            self.update_car(car_id)
        ).pack(pady=10)

        tk.Button(
            self.root,
            text="Back to Manage Cars",
            width=20,
            command=self.manage_cars
        ).pack()

    def update_car(self, car_id):
        """Update an existing car."""

        make = self.update_make_entry.get().strip()
        model = self.update_model_entry.get().strip()
        year = self.update_year_entry.get().strip()
        mileage = self.update_mileage_entry.get().strip()
        min_period = self.update_min_period_entry.get().strip()
        max_period = self.update_max_period_entry.get().strip()
        daily_rate = self.update_daily_rate_entry.get().strip()

        if not all([
            make,
            model,
            year,
            mileage,
            min_period,
            max_period,
            daily_rate
        ]):
            messagebox.showwarning(
                "Missing Information",
                "Please complete all fields."
            )
            return

        try:
            year = int(year)
            mileage = int(mileage)
            min_period = int(min_period)
            max_period = int(max_period)
            daily_rate = float(daily_rate)

        except ValueError:
            messagebox.showerror(
                "Invalid Information",
                "Please enter valid numbers."
            )
            return

        if min_period > max_period:
            messagebox.showerror(
                "Invalid Rental Period",
                "Minimum rental period cannot be greater "
                "than maximum rental period."
            )
            return

        if daily_rate <= 0:
            messagebox.showerror(
                "Invalid Daily Rate",
                "Daily rate must be greater than zero."
            )
            return

        car_service = CarService()

        car_service.update_car(
            car_id,
            make,
            model,
            year,
            mileage,
            min_period,
            max_period,
            daily_rate
        )

        car_service.close()

        messagebox.showinfo(
            "Success",
            "Car updated successfully!"
        )

        self.manage_cars()

    # =========================================================
    # NAVIGATION
    # =========================================================

    def back_to_admin_dashboard(self):
        """Return to the admin dashboard."""

        if (
            self.current_user
            and self.current_user.role == "admin"
        ):
            self.create_admin_dashboard(
                self.current_user
            )

    def logout(self):
        """Log the current user out."""

        self.current_user = None
        self.create_login_screen()

    def close_application(self):
        """Close the application."""

        self.user_service.close()
        self.root.destroy()


def main():
    """Start the Car Rental System."""

    root = tk.Tk()

    app = CarRentalApp(root)

    root.protocol(
        "WM_DELETE_WINDOW",
        app.close_application
    )

    root.mainloop()


if __name__ == "__main__":
    main()