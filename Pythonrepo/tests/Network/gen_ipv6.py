def generate_ipv6_addresses(ip_prefix, start_suffix, end_suffix, format='decimal'):
    """
    Generate IPv6 addresses with a given prefix, start suffix, and end suffix.
    Args:
    ip_prefix (str): The prefix for the IPv6 addresses.
    start_suffix (int): The starting suffix in decimal.
    end_suffix (int): The ending suffix in decimal.
    format (str): The format for the suffix in the IP address, either 'decimal' or 'hex'.
    Returns:
    List of IPv6 addresses in the specified format.
    """
    ipv6_addresses = []

    # Iterate through the range from start to end (inclusive)
    for suffix in range(start_suffix, end_suffix + 1):
        # Convert suffix to desired format
        if format == 'hex':
            # Convert suffix to hexadecimal and remove the '0x' prefix
            suffix_str = f"{suffix:x}"
        elif format == 'decimal':
            # Convert suffix to decimal string
            suffix_str = str(suffix)
        else:
            raise ValueError("Invalid format specified. Use 'decimal' or 'hex'.")

        # Construct the IPv6 address
        ipv6_address = f"{ip_prefix}:{suffix_str}"

        # Append the address to the list
        ipv6_addresses.append(ipv6_address)

    return ipv6_addresses

# Example usage:
ip_prefix = "fdca:f995:220a:a00::110"
start_suffix = 65532
end_suffix = 65535

# Choose 'decimal' or 'hex' format for the suffix
format_choice = 'hex'  # or 'hex'

# Generate IPv6 addresses
addresses = generate_ipv6_addresses(ip_prefix, start_suffix, end_suffix, format=format_choice)

# Print the generated addresses
for address in addresses:
    print(address)