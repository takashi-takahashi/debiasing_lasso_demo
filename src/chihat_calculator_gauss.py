import numpy as np


def calc_chi_hat(α, rss):
    return rss * α


def calc_g_prime(χ, α):
    return (α / 2) * __get_fraction(1.0, 1.0 + χ)


def calc_g_two_prime(χ, α):
    return (α / 2) * __get_fraction(1.0, (1.0 + χ) ** 2)


def calc_z(χ, α):
    φ = calc_phi(χ=χ, α=α)
    return -1.0 * __get_fraction(numerator=1.0 - χ + φ, denominator=2.0 * χ)


def calc_z_prime(χ, α):
    φ = calc_phi(χ=χ, α=α)
    return -1.0 * __get_fraction(numerator=1.0 + χ - 2.0 * α * χ + φ,
                                 denominator=2.0 * χ * χ * φ)


def calc_phi(χ, α):
    return np.sqrt((1.0 + χ) ** 2 - 4.0 * α * χ)


def __get_fraction(numerator, denominator):
    return numerator / denominator
