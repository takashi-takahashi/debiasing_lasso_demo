import numpy as np


def calc_chi_hat(χ, α, rss, σ):
    g_two_prime = calc_g_two_prime(χ, α)
    g_prime = calc_g_prime(χ, α)

    numerator = α * g_two_prime * rss - g_two_prime * α * (σ ** 2) + 2.0 * (σ ** 2) * (g_prime ** 2)

    denominator = g_prime - g_two_prime * χ
    return __get_fraction(numerator, denominator)


def calc_g_prime(χ, α):
    return (1 / 2) * (calc_z(χ=χ, α=α) + 1 / χ)


def calc_g_two_prime(χ, α):
    return (1 / 2) * (calc_z_prime(χ=χ, α=α) + 1 / (χ ** 2))


def calc_z(χ, α):
    φ = calc_phi(χ=χ, α=α)
    return -1.0 * __get_fraction(1.0 - χ + φ, 2.0 * χ)  # eigenvalue is one and zero


def calc_z_prime(χ, α):
    φ = calc_phi(χ=χ, α=α)
    return -1.0 * __get_fraction(1.0 + χ - 2.0 * α * χ + φ,
                                 2.0 * χ * χ * φ)  # eigenvalue is one and zero


def calc_phi(χ, α):
    return np.sqrt((1.0 + χ) ** 2 - 4.0 * α * χ)  # eigenvalue is one and zero


def __get_fraction(numerator, denominator):
    return numerator / denominator
