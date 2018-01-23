import sys


pmt_per_dom = 31
dom_per_du = 18
du_per_block = 115


def pmt_id_to_storey(pmt_id):
    storey = dom_per_du - int(int(pmt_id % (pmt_per_dom * dom_per_du)) / pmt_per_dom)
    return storey


class Event(object):
    def __init__(self):
        self.pmt_id_list = list()
        self.time_list = list()

    def sort_by_time(self):
        return sorted(zip(self.time_list, self.pmt_id_list), key=lambda x: x[0])

    def __len__(self):
        if len(self.pmt_id_list) == len(self.time_list):
            print("ERROR: inconsitent data")
            sys.exit(-1)
        return len(self.pmt_id_list)


class EvtFile(object):
    def __init__(self, filename):
        self.file = open(filename, "r")

    def __iter__(self):
        return self

    def __next__(self):
        return self.read_event()

    def read_event(self):
        while True:
            line = self.file.readline()
            if not line:
                return StopIteration
            line_split = line.split()
            if line_split[0] == "start_event:":
                event = Event()
            if line_split[0] == "hit:":
                event.pmt_id_list.append(int(line_split[2]))
                event.time_list.append(float(line_split[4]))
            if line_split[0] == "end_event:":
                try:
                    return event
                except:
                    pass
