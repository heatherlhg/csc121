## Calculate jackpot payout options pre and post tax.

jackpot = float(input('What was the jackpot amount? (digits only, no commas) '))

annual_pretax = jackpot/20
annual_net = annual_pretax * 0.70
lump_pretax = jackpot * 0.65
lump_net = lump_pretax * 0.70

print('Annual payout before tax $',format(annual_pretax,'.2f'))
print('Annual payout after tax $',format(annual_net, '.2f'))
print('Lump sum payout before tax $',format(lump_pretax, '.2f'))
print('Lump sum payout after tax $',format(lump_net,'.2f'))
