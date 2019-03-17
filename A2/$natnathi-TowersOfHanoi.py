
import argparse
import sys


parser = argparse.ArgumentParser(prog= "Towers of Hanoi Program", description="Enter the desired number of disks and redirect the stderr to a new file to get the total number of movements in a seperate file")
parser.add_argument("-n","--number", type=int, required=True, help="Your desired number of disks")
args = parser.parse_args()


def towers(n, from_disk, aux_disk, to_disk):
    global count
    count += 1

    if n == 1:
        print("Move disk from {} to {}.".format(from_disk, to_disk))
    else:
        towers(n-1, from_disk, to_disk, aux_disk)
        print("Move disk from {} to {}.".format(from_disk, to_disk))
        towers(n-1, aux_disk, from_disk, to_disk)


if __name__ == '__main__':
    count = 0
    towers(args.number, 'A', 'B', 'C')
    print >> sys.stderr, count

