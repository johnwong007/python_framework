FUNCTIONS
    a2b_base64(...)
        (ascii) -> bin. Decode a line of base64 data

    a2b_hex(...)
        a2b_hex(hexstr) -> s; Binary data of hexadecimal representation.

        hexstr must contain an even number of hex digits (upper or lower case).
        This function is also available as "unhexlify()"

    a2b_hqx(...)
        ascii -> bin, done. Decode .hqx coding

    a2b_qp(...)
        Decode a string of qp-encoded data

    a2b_uu(...)
        (ascii) -> bin. Decode a line of uuencoded data

    b2a_base64(...)
        (bin) -> ascii. Base64-code line of data

    b2a_hex(...)
        b2a_hex(data) -> s; Hexadecimal representation of binary data.

        This function is also available as "hexlify()".

    b2a_hqx(...)
        Encode .hqx data

    b2a_qp(...)
        b2a_qp(data, quotetabs=0, istext=1, header=0) -> s;
         Encode a string using quoted-printable encoding.

        On encoding, when istext is set, newlines are not encoded, and white
        space at end of lines is.  When istext is not set, \r and \n (CR/LF) are
        both encoded.  When quotetabs is set, space and tabs are encoded.

    b2a_uu(...)
        (bin) -> ascii. Uuencode line of data

    crc32(...)
        (data, oldcrc = 0) -> newcrc. Compute CRC-32 incrementally

    crc_hqx(...)
        (data, oldcrc) -> newcrc. Compute hqx CRC incrementally

    hexlify(...)
        b2a_hex(data) -> s; Hexadecimal representation of binary data.

        This function is also available as "hexlify()".

    rlecode_hqx(...)
        Binhex RLE-code binary data

    rledecode_hqx(...)
        Decode hexbin RLE-coded string

    unhexlify(...)
        a2b_hex(hexstr) -> s; Binary data of hexadecimal representation.

        hexstr must contain an even number of hex digits (upper or lower case).
        This function is also available as "unhexlify()"

