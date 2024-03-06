import tkinter as tk
import time
import random

class VehicleCounterApp:
    def __init__(self, master, car_count, bus_count,motorcycle_count,truck_count, lane=1):
        self.master = master
        self.lane = lane
        self.master.title(f"Lane {lane}")

        self.motorcycle_count = motorcycle_count
        self.car_count = car_count
        self.bus_count = bus_count
        self.truck_count = truck_count


        
        self.label_motorcycles = tk.Label(master, text="Motorcycles: " + str(self.motorcycle_count))
        self.label_motorcycles.pack()

        self.label_cars = tk.Label(master, text="Cars: " + str(self.car_count))
        self.label_cars.pack()

        self.label_buses = tk.Label(master, text="Buses: " + str(self.bus_count))
        self.label_buses.pack()

        self.label_trucks = tk.Label(master, text="Trucks: " + str(self.truck_count))
        self.label_trucks.pack()



        self.entry_motorcycle = tk.Entry(master, textvariable=self.motorcycle_count)
        self.entry_motorcycle.pack()

        self.entry_car = tk.Entry(master, textvariable=self.car_count)
        self.entry_car.pack()

        self.entry_bus = tk.Entry(master, textvariable=self.bus_count)
        self.entry_bus.pack()

        self.entry_truck = tk.Entry(master, textvariable=self.truck_count)
        self.entry_truck.pack()


def main():
    global motorcycle_count,car_count,bus_count,truck_count
    motorcycle_count = 0
    car_count = 0
    bus_count = 0
    truck_count = 0

    global motorcycle_count,car_count,bus_count,truck_count


    root = tk.Tk()
    app = VehicleCounterApp(root,motorcycle_count,car_count,bus_count,truck_count)

    def update_counts():
        global motorcycle_count,car_count,bus_count,truck_count
        motorcycle_count = random.randrange(25)
        car_count = random.randrange(25)
        bus_count = random.randrange(9)
        truck_count = random.randrange(9)

        app.label_motorcycles.config(text="Motorcycles: " + str(motorcycle_count))
        app.label_cars.config(text="Cars: " + str(car_count))
        app.label_buses.config(text="Buses: " + str(bus_count))
        app.label_trucks.config(text="Trucks: " + str(truck_count))
        root.after(100, update_counts)
    
    update_counts()
    root.mainloop()

    
    

if __name__ == "__main__":
    main()
