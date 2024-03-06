import tkinter as tk
import time
import random


active_lane = 1  # Initially set to Lane 1


def appStart():

    global motorcycle, car, bus, truck
    global total_units

    motorcycle = [0,30,29,27,19]
    car = [0,25,27,19,21]
    bus = [0,10,13,9,9]
    truck = [0,7,5,3,8]
    total_units = [0,0,0,0,0]


    root = tk.Tk()


    app1 = VehicleCounterApp(root, motorcycle[1], car[1], bus[1], truck[1], lane=1)
    app2 = VehicleCounterApp(tk.Toplevel(root),motorcycle[2], car[2], bus[2], truck[2], lane=2)
    app3 = VehicleCounterApp(tk.Toplevel(root),motorcycle[3], car[3], bus[3], truck[3], lane=3)
    app4 = VehicleCounterApp(tk.Toplevel(root), motorcycle[4], car[4], bus[4], truck[4], lane=4)


    def update_counts():
        global motorcycle, car, bus, truck
        global active_lane


        update_lane_label(app1, 1)
        update_lane_label(app2, 2)
        update_lane_label(app3, 3)
        update_lane_label(app4, 4)


        update_lane_counts(app1,motorcycle, car, bus, truck,1)
        update_lane_counts(app2,motorcycle, car, bus, truck,2)
        update_lane_counts(app3,motorcycle, car, bus, truck,3)
        update_lane_counts(app4,motorcycle, car, bus, truck,4)


        root.after(1000, update_counts)  


    def update_lane_label(app, lane_num):
        app.label_lane.config(text="Lane " + str(lane_num))
        app.label_signal.config(bg="green" if active_lane == lane_num else "red")


    def update_lane_counts(app, motorcycle, car, bus, truck,lane):
        global active_lane
        global total_units

        total_units[lane] = 2 * motorcycle[lane] + 4 * car[lane] + 8 * bus[lane] + 8 * truck[lane]

        if active_lane==lane:
            motorcycle[lane] = max(0,motorcycle[lane]-1)
            car[lane] = max(0,car[lane]-1)
            bus[lane] = max(0,bus[lane]-1)
            truck[lane] = max(0,truck[lane]-1)
        else:
            motorcycle[lane] += random.randrange(0,5)
            car[lane] += random.randrange(0,3)
            bus[lane] += random.randrange(0,2)
            truck[lane] += random.randrange(0,2)
            


        # time_remaining = 0
        # if active_lane == app.lane:
            # time_remaining = total_units * 0.05
            # if time_remaining > 0:
            #     if app.label_signal["bg"] == "green":
            #         # if motorcycle_count>=1:
            #         motorcycle[lane] -= 1
            #         car[lane] -= 1
            #         bus[lane] -= 1
            #         truck[lane] -= 1
            #     else:
            #         motorcycle[lane] += 1
            #         car[lane] += 1
            #         bus[lane] += 1
            #         truck[lane] += 1


        app.label_motorcycles.config(text="Motorcycles: " + str(motorcycle[lane]))
        app.label_cars.config(text="Cars: " + str(car[lane]))
        app.label_buses.config(text="Buses: " + str(bus[lane]))
        app.label_trucks.config(text="Trucks: " + str(truck[lane]))
        app.label_total_units.config(text="Total Units: " + str(total_units[lane]))
        # if lane==active_lane:
        #     app.label_time_remaining.config(text="Time Remaining: " + "{:.2f}".format() if  > 0 else "")
        # else:
        #     app.label_time_remaining.config(text="Time Remaining: " + "{:.2f}".format() if  > 0 else "")



    update_counts()
    root.mainloop()




class VehicleCounterApp:
    def __init__(self, master, motorcycle_count,car_count, bus_count, truck_count, lane):
        self.master = master
        self.lane = lane
        self.master.title(f"Lane {lane}")


        self.motorcycle_count = motorcycle_count
        self.car_count = car_count
        self.bus_count = bus_count
        self.truck_count = truck_count


        # Create labels for lane name, signal light color, vehicle counts, total units, and time remaining
        self.label_lane = tk.Label(master, text="Lane " + str(lane))
        self.label_lane.pack()


        self.label_signal = tk.Label(master, width=10, height=2)  # Set appropriate width and height
        self.label_signal.pack()


        self.label_motorcycles = tk.Label(master, text="Motorcycles: " + str(self.motorcycle_count))
        self.label_motorcycles.pack()


        self.label_cars = tk.Label(master, text="Cars: " + str(self.car_count))
        self.label_cars.pack()


        self.label_buses = tk.Label(master, text="Buses: " + str(self.bus_count))
        self.label_buses.pack()


        self.label_trucks = tk.Label(master, text="Trucks: " + str(self.truck_count))
        self.label_trucks.pack()


        self.label_total_units = tk.Label(master, text="Total Units: ")
        self.label_total_units.pack()


        self.label_time_remaining = tk.Label(master, text="Time Remaining: ")
        self.label_time_remaining.pack()


        self.entry_motorcycle = tk.Entry(master, textvariable=self.motorcycle_count)
        self.entry_motorcycle.pack()


        self.entry_car = tk.Entry(master, textvariable=self.car_count)
        self.entry_car.pack()


        self.entry_bus = tk.Entry(master, textvariable=self.bus_count)
        self.entry_bus.pack()


        self.entry_truck = tk.Entry(master, textvariable=self.truck_count)
        self.entry_truck.pack()




appStart()



