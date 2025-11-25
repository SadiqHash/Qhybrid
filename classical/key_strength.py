def evaluate_key_strength(bits):
    """Return a tiny estimation dict for demo purposes."""
    grover_effective = max(bits // 2, 1)
    return {
        "original_bits": bits,
        "grover_effective_bits": grover_effective,
        "recommendation": "Increase key size for higher quantum safety."
    }
