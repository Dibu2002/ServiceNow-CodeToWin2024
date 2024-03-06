import tkinter as tk
import random

class MaxHeap:
    def __init__(self, arr=None):
        self.heap = []
        if type(arr) is list:
            self.heap = arr.copy()
            for i in range(len(self.heap))[::-1]:
                self._siftdown(i)

    def _siftup(self, i):
        parent = (i-1)//2
        while i != 0 and self.heap[i] > self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = (i-1)//2

    def _siftdown(self, i):
        left = 2*i + 1
        right = 2*i + 2
        while (left < len(self.heap) and self.heap[i] < self.heap[left]) or (right < len(self.heap) and self.heap[i] < self.heap[right]):
            biggest = left if (right >= len(self.heap) or self.heap[left] > self.heap[right]) else right
            self.heap[i], self.heap[biggest] = self.heap[biggest], self.heap[i]
            i = biggest
            left = 2*i + 1
            right = 2*i + 2

    def insert(self, element):
        self.heap.append(element)
        self._siftup(len(self.heap)-1)

    def get_max(self):
        return self.heap[0] if len(self.heap) > 0 else None

    def extract_max(self):
        if len(self.heap) == 0:
            return None
        maxval = self.heap[0]
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop()
        self._siftdown(0)
        return maxval

    def update_by_index(self, i, new):
        old = self.heap[i]
        self.heap[i] = new
        if new > old:
            self._siftup(i)
        else:
            self._siftdown(i)

    def update(self, old, new):
        if old in self.heap:
            self.update_by_index(self.heap.index(old), new)


class PriorityQueue:
    def __init__(self):
        self.queue = MaxHeap()

    def enqueue(self, element):
        self.queue.insert(element)

    def peek(self):
        return self.queue.get_max()

    def dequeue(self, element):
        return self.queue.extract_max()

    def is_empty(self):
        return len(self.queue.heap) == 0

    def change_priority_by_index(self, i, new):
        self.queue.update_by_index(i, new)

    def change_priority(self, old, new):
        self.queue.update(old, new)

def total_units_count(motorcycle, car, bus, truck):
    return 2 * motorcycle + 4 * car + 8 * bus + 8 * truck


class TrafficLane:
    def __init__(self, master, motorcycle_count,car_count, bus_count, truck_count, lane, estimated_green_time):
        self.master = master
        self.lane = lane
        self.master.title(f"Lane {lane}")
        self.motorcycle_count = motorcycle_count
        self.car_count = car_count
        self.bus_count = bus_count
        self.truck_count = truck_count
        self.lane_id = lane
        self.current_time_left = 0
        self.estimated_green_time = estimated_green_time
        self.waiting_time = 0
        self.priority = 0
        self.important_vehicle_present = 0    #  1 for true, 0 for false
        self.calculate_priority()

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

    def calculate_priority(self):
        self.priority = 0.3*self.estimated_green_time + 0.7*self.waiting_time + 1000*self.important_vehicle_present

    def update_red_light(self, other_lane_green_time):
        self.estimated_green_time = int(total_units_count(motorcycle[self.lane_id], car[self.lane_id], bus[self.lane_id], truck[self.lane_id]) * 0.05)
        self.waiting_time += other_lane_green_time

    def grant_green_light(self):
        self.current_time_left = self.estimated_green_time
        self.estimated_green_time = int(total_units_count(motorcycle[self.lane_id], car[self.lane_id], bus[self.lane_id], truck[self.lane_id]) * 0.05)
        self.current_light_state = True

global active_lane, highest_priority_lane     # Initially set to Lane 1
global green_time_current, green_time_val
global next_active_lane,next_green_time

global motorcycle, car, bus, truck
global total_units

motorcycle = [0,15,29,18,21]
car = [0,12,7,10,11]
bus = [0,1,3,2,2]
truck = [0,2,1,2,3]
total_units = [0,0,0,0,0]

root = tk.Tk()

app1 = TrafficLane(root, motorcycle[1], car[1], bus[1], truck[1], lane=1, estimated_green_time=int(total_units_count(motorcycle[1], car[1], bus[1], truck[1]) * 0.18))
app2 = TrafficLane(tk.Toplevel(root),motorcycle[2], car[2], bus[2], truck[2], lane=2, estimated_green_time = int(total_units_count(motorcycle[2], car[2], bus[2], truck[2]) * 0.05))
app3 = TrafficLane(tk.Toplevel(root),motorcycle[3], car[3], bus[3], truck[3], lane=3, estimated_green_time=int(total_units_count(motorcycle[3], car[3], bus[3], truck[3]) * 0.05))
app4 = TrafficLane(tk.Toplevel(root), motorcycle[4], car[4], bus[4], truck[4], lane=4, estimated_green_time=int(total_units_count(motorcycle[4], car[4], bus[4], truck[4]) * 0.05))

lanes = [app1, app2, app3, app4]
priority_queue = PriorityQueue()

def put_all_in_queue(other_lane_time, lane_id):
    # change green
    for lane in lanes:
        if lane.lane_id == lane_id:
            lane.grant_green_light
        else:
            lane.update_red_light(other_lane_time)
        lane.calculate_priority()
        priority_queue.enqueue((lane.priority, lane.lane_id))

def remove_all_from_queue():
    while(priority_queue.is_empty() == False) :
      pri, lane_id = priority_queue.dequeue(None)

def get_which_lane(lane_id):
    for lane in lanes:
        if(lane.lane_id == lane_id):
            return lane
def get_active_lane():
    global active_lane, highest_priority_lane
    global green_time_current, green_time_val
    global next_active_lane,next_green_time
    highest_priority, highest_priority_lane_id = priority_queue.dequeue(None)
    next_active_lane = highest_priority_lane_id
    highest_priority_lane = get_which_lane(highest_priority_lane_id)
    next_green_time = highest_priority_lane.estimated_green_time
    remove_all_from_queue()

active_lane = 1
green_time_current = app1.estimated_green_time
green_time_val = green_time_current
put_all_in_queue(green_time_current, active_lane)

def appStart():

    def update_counts():
        global motorcycle, car, bus, truck
        global active_lane
        global next_active_lane

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
        global green_time_current, green_time_val
        global next_active_lane

        total_units[lane] = total_units_count(motorcycle[lane], car[lane], bus[lane], truck[lane])

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
        app.label_motorcycles.config(text="Motorcycles: " + str(motorcycle[lane]))
        app.label_cars.config(text="Cars: " + str(car[lane]))
        app.label_buses.config(text="Buses: " + str(bus[lane]))
        app.label_trucks.config(text="Trucks: " + str(truck[lane]))
        app.label_total_units.config(text="Total Units: " + str(total_units[lane]))

        if lane == active_lane:
            if(green_time_current == 5):
                put_all_in_queue(green_time_val, active_lane)
                get_active_lane()
            if(green_time_current == 1):
                active_lane = next_active_lane
                green_time_current = next_green_time
                green_time_val = green_time_current
            else:
                green_time_current -= 1
                app.label_time_remaining.config(text="Time Remaining: " + str(green_time_current))
        else:
            
            app.label_time_remaining.config(text="Last Green Estimated Time: " + str(app.estimated_green_time))

    update_counts()
    root.mainloop()

appStart()


