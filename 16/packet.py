from os import read
import math


with open('data.txt', 'r') as file:
    data = file.read().split('\n')

# cut trailing newline
data.pop(-1)

# Further data processing

# convert string of chars into binary

# Simplest way to get them all in binary with 4 digits

hex_to_bin = {
    '0' : '0000',
    '1' : '0001',
    '2' : '0010',
    '3' : '0011',
    '4' : '0100',
    '5' : '0101',
    '6' : '0110',
    '7' : '0111',
    '8' : '1000',
    '9' : '1001',
    'A' : '1010',
    'B' : '1011',
    'C' : '1100',
    'D' : '1101',
    'E' : '1110',
    'F' : '1111',
}


# int_array = [int(e, 16) for e in data[0]]

bin_array = [hex_to_bin[e] for e in data[0]]

bin_string = "".join(e for e in bin_array)

# breakpoint()

# Part 1

# def read_stream(packet, amount):
#     read = packet[:amount]
#     packet = packet[amount:]

#     return read, packet

# def parse_packet(packet, version_sum):
#     # print(packet)
#     if packet == "":
#         return version_sum, packet
#     if '1' not in packet:
#         return version_sum, packet
#     version, packet = read_stream(packet, 3)
#     type, packet = read_stream(packet, 3)

#     length = None

#     # breakpoint()

#     version_sum = int(version, 2) + version_sum

#     # subpackets.append(packet)
#     # breakpoint()
#     # print('0' + type != hex_to_bin['4'])
#     if '0' + type != hex_to_bin['4']:
#         length_type_id, packet = read_stream(packet, 1)
#         if length_type_id == '0':
#             length_of_sub_packets_bits, packet = read_stream(packet, 15)
#             rem_length_of_sub_packets = int(length_of_sub_packets_bits, 2)
#             # breakpoint()
#             # While...?
#             while rem_length_of_sub_packets != 0:
#                 if rem_length_of_sub_packets < 0:
#                     print("ERROR")
#                     breakpoint()

#                 # breakpoint()
#                 len_before = len(packet)
#                 version_sum, packet = parse_packet(packet, version_sum)
#                 consumed = len_before - len(packet)
#                 rem_length_of_sub_packets -= consumed
#                 # breakpoint()
#                 # print("END While")


#             # breakpoint()
#         else: # '1'
#             number_of_sub_packets_bits, packet = read_stream(packet, 11)
#             number_of_sub_packets = int(number_of_sub_packets_bits, 2)

#             for _ in range(number_of_sub_packets):
#                 version_sum, packet = parse_packet(packet, version_sum)

#     else:

#         # breakpoint()
#         bin_numbers = []
#         cont = True
#         while cont:
#             prefix, packet = read_stream(packet, 1)
#             if prefix == '0':
#                 cont = False

#             number_bits, packet = read_stream(packet, 4)

#             bin_numbers.append(number_bits)

#         # breakpoint()

#     return version_sum, packet


# version_sum, packet = parse_packet(bin_string, 0)

# print(version_sum)

# # breakpoint()


# Part 2

def read_stream(packet, amount):
    read = packet[:amount]
    packet = packet[amount:]

    return read, packet

def parse_packet(packet, version_sum):
    # print(packet)
    if packet == "":
        return version_sum, packet
    if '1' not in packet:
        return version_sum, packet


    version, packet = read_stream(packet, 3)
    version_num = int(version, 2)
    type, packet = read_stream(packet, 3)
    type_num = int(type, 2)

    length = None

    # breakpoint()

    version_sum = int(version, 2) + version_sum

    # subpackets.append(packet)
    # breakpoint()
    # print('0' + type != hex_to_bin['4'])
    values = []
    if '0' + type != hex_to_bin['4']:
        length_type_id, packet = read_stream(packet, 1)
        if length_type_id == '0':
            length_of_sub_packets_bits, packet = read_stream(packet, 15)
            rem_length_of_sub_packets = int(length_of_sub_packets_bits, 2)
            # breakpoint()
            # While...?
            while rem_length_of_sub_packets != 0:
                if rem_length_of_sub_packets < 0:
                    print("ERROR")
                    breakpoint()

                # breakpoint()
                len_before = len(packet)
                version_sum, packet, value = parse_packet(packet, version_sum)
                values.append(value)
                consumed = len_before - len(packet)
                rem_length_of_sub_packets -= consumed
                # breakpoint()
                # print("END While")


            # breakpoint()
        else: # '1'
            number_of_sub_packets_bits, packet = read_stream(packet, 11)
            number_of_sub_packets = int(number_of_sub_packets_bits, 2)
            for _ in range(number_of_sub_packets):
                version_sum, packet, value = parse_packet(packet, version_sum)
                values.append(value)

    else:

        # breakpoint()
        bin_numbers = []
        cont = True
        while cont:
            prefix, packet = read_stream(packet, 1)
            if prefix == '0':
                cont = False

            number_bits, packet = read_stream(packet, 4)

            bin_numbers.append(number_bits)

        values.append(int("".join(e for e in bin_numbers), 2))

        # breakpoint()
    # breakpoint()
    # Contrary to what the internet says, I don't think this is efficient
    # it calculates all of these every time

    # and I shouldn't have tried to hack it to fix it

    # if len(values) == 1:
    #     values.append(0) # Hack to make the bad switch work
            # this breaks product for 1 value
    # switcher = {
    #     0: sum(values), # sum packet
    #     1: math.prod(values),# product packet
    #     2: min(values),
    #     3: max(values),
    #     4: values[0],
    #     5: 1 if values[0] > values[1] else 0,
    #     6: 1 if values[0] < values[1] else 0,
    #     7: 1 if values[0] == values[1] else 0
    # }
    # breakpoint()


    if type_num == 0: value = sum(values) # sum packet
    if type_num == 1: value = math.prod(values)# product packet
    if type_num == 2: value = min(values)
    if type_num == 3: value = max(values)
    if type_num == 4: value = values[0]
    if type_num == 5: value = 1 if values[0] > values[1] else 0
    if type_num == 6: value = 1 if values[0] < values[1] else 0
    if type_num == 7: value = 1 if values[0] == values[1] else 0

    return version_sum, packet, value


version_sum, packet, value = parse_packet(bin_string, 0)

print(value)

# breakpoint()
