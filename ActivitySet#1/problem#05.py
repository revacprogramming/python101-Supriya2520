def computepay(h, r):
    if h > 40 :
        reg = r * h
        otp = (h - 40.0) * (r * 0.5)
        pay = reg + otp
    else:
        pay = h * r
    return pay
sh = input ("enter h:")
sr = input ("enter r:")
fh = float(sh)
fr = float(sr)

xp = computepay(fh,fr)

print("Pay:",xp)
