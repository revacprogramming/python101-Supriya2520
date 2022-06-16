def computepay(h, r):
  
    if h > 40 :
        a = r * h
        b = (h - 40.0) * (r * 0.5)
        pay = a + b
    else:
        pay = h * r
    return Pay
sh = input ("enter h:")
sr = input ("enter r:")
fh = float(sh)
fr = float(sr)
xp = computepay(fh,fr)
print("Pay:",xp)
