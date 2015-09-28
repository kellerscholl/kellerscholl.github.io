# main will take in inputs from sliders on how the sharing economy will 
# impact different industries, and the fraction of the economy that
# those industries represent, and report over the next ten time periods the
# impact on GDP and unemployment of the changes predicted to come from
# the sharing economy.
# This is a first sketch, reliant on simplistic models, but it helps
# illustrate the potential impact of changes

def transform_input_from_sliders(updated_labor_list, updated_capital_list, industry_weights):
	weighted_list = [a*c,b*c for a,b,c in zip(updated_labor_list,
		updated_capital_list,industry_weights)]
	E_l = sum(a[0] for a in weighted_list)
	E_k = sum(a[1] for a in weighted_list)
	return E_l,E_k
def new_k(Y, K):
	# p1 for the US is estimated at 12.8% 
	# https://en.wikipedia.org/wiki/List_of_countries_by_gross_fixed_investment_as_percentage_of_GDP
	# p2 is estimated at 10% to start with. 
	# return Y*p1-K*p2
	# We're not presently in equilibrium state, the economy is growing.
	# We currently have roughly ten times as much capital as we do national income.
	# http://rutledgecapital.com/2009/05/24/total-assets-of-the-us-economy-188-trillion-134xgdp/
	# So this model is of merely limited utility.
	# But it's still an interesting exploration of the first order impacts.
	return Y*.128-K*.1
def time_unit_change(x):
	return (x-1)/10
def Y(E_k,E_l,K,L=16.8,alpha=.26):
	return (E_k * K)**alpha (E_l * L)**(1-alpha)
def main(updated_labor_list, updated_capital_list):
	final_E_l,final_E_k = transform_input_from_sliders(updated_labor_list, 
		updated_capital_list, industry_weights)
	E_l, E_k = 1,1
	L = 16.8 # Assume that Y doesn't actually change over ten years is 
	# reasonable given aging population. This value is never actually used
	K = 12.8
	Y = initial_Y = 10

	# These values are slightly approximate, but accurate to the numbers given.
	for i in range(10):
		E_l += time_unit_change(final_E_l)
		E_k += time_unit_change(final_E_k)
		Y = Y(E_k,E_l,K,L)
		K = new_K(K,Y)
		#Display pretty things?
		print("Total economic output in this year is")
		print(Y)
		print("Unemployment, absent federal reserve bank action, would be predicted at")
		print(10-((Y/initial_Y)*100/2)/i)