#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    packet_factory.py
    Author: Aidin Lehrman
    
     0               1               2               3
 	 0 1 2 3 4 5 6 7 0 1 2 3 4 5 6 7 0 1 2 3 4 5 6 7 0 1 2 3 4 5 6 7
	+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
	|           Source ID           |        Destination ID         |
	+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
	|                        Sequence Number                        |
	+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
	|                    Acknowledgment Number                      |
	+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
	|  Data |       |C|E|U|A|P|R|S|F|                               |
	| Offset|0 0 0 0|W|C|R|C|S|S|Y|I|          Window Size          |
	|       |       |R|E|G|K|H|T|N|N|                               |
	+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
	|           Checksum            |         Urgent Pointer        |
	+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
	|                    Options                    |    Padding    |
	+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
	|                             Data                              |
	+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
"""

class Packet:
    """ Packet Class
    
    Constructs Packets to be sent by MicroBit
    
    Attributes:
		source_id (int): 
		destination_id  (int): 
        sequence_number (int): 
        acknowledgement_number (int): 
        flags (int): 
        window_size (int): 
        checksum (int): 
        urgent_pointer (int): 
        options (int):
    """

    source_id: int
    destination_id: int
    sequence_number: int
    acknowledgement_number: int
    flags: int
    window_size: int
    checksum: int
    urgent_pointer: int
    options: int

    def __init__(self, source_id: int = 0, destination_id: int = 0, \
        sequence_number: int = 0, acknowledgement_number: int = 0, \
            flags: int = 0, window_size: int = 0, checksum: int = 0, \
                urgent_pointer: int = 0, options: int = 0) -> None:
        pass

    def __str__(self) -> str:
        """ To String Function
        """
        return ''

    def to_bytes(self) -> bytes:
        """ Converts Packet to List of Bytes
        """
        return bytes(b'\x00')
