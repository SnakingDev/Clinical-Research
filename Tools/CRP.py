from math import sqrt
from scipy.stats import norm

old_n = 131
new_n = 400
p_value = 0.126

def onesided_conditional_replication_probability(m,n,p):
    a = sqrt(n/(m+n))
    b = sqrt(m/n)*1.645
    z_value = norm.ppf(1-p)
    d = a*(b - z_value)
    e = 1 - norm.cdf(d)
    print("The conditional replication probability estimate (one-sided) for:")
    print(f"Old population (m) = {old_n}")
    print(f"New population (n) = {new_n}")
    print(f"p value = {p_value}")
    print(f"is {e:.4f}")

def twosided_conditional_replication_probability(m,n,p):
    a = sqrt(n/(m+n))
    b = sqrt(m/n)*1.96
    z_value = norm.ppf(1-p)
    d = a*(b - z_value)
    e = 1 - norm.cdf(d)
    print("The conditional replication probability estimate (two-sided) for:")
    print(f"Old population (m) = {old_n}")
    print(f"New population (n) = {new_n}")
    print(f"p value = {p_value}")
    print(f"is {e:.4f}")

onesided_conditional_replication_probability(old_n, new_n, p_value)
twosided_conditional_replication_probability(old_n, new_n, p_value)

