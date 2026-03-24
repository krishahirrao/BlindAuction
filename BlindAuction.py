def find_highest_bidder(bidding):
    highest_bid = 0
    winner = ""
    for bidder in bidding:
        bid_amount = bidding[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ₹{highest_bid}")

bid = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name?: ")
    price = float(input("What is your bid?: ₹"))
    bid[name] = price
    next_bid = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if next_bid == 'no':
        continue_bidding = False
        find_highest_bidder(bid)
    elif next_bid == 'yes':
        print("\n"* 50)