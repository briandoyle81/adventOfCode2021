from os import read


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
    type, packet = read_stream(packet, 3)

    length = None

    # breakpoint()

    version_sum = int(version, 2) + version_sum

    # subpackets.append(packet)
    # breakpoint()
    # print('0' + type != hex_to_bin['4'])
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
                version_sum, packet = parse_packet(packet, version_sum)
                consumed = len_before - len(packet)
                rem_length_of_sub_packets -= consumed
                # breakpoint()
                # print("END While")


            # breakpoint()
        else: # '1'
            number_of_sub_packets_bits, packet = read_stream(packet, 11)
            number_of_sub_packets = int(number_of_sub_packets_bits, 2)

            for _ in range(number_of_sub_packets):
                version_sum, packet = parse_packet(packet, version_sum)

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

        # breakpoint()

    return version_sum, packet


version_sum, packet = parse_packet(bin_string, 0)

print(version_sum)

# breakpoint()
