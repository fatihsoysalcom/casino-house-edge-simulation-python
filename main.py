import random

def simulate_casino_game(num_rounds, player_starting_balance=1000, casino_starting_balance=1000):
    """
    Simulates a simple coin flip game to demonstrate the casino's house edge.
    Player bets $1 on 'Heads'.
    If 'Heads', player wins $1.95 (net profit $0.95).
    If 'Tails', player loses $1.
    The actual coin flip is 50/50.
    """
    player_balance = player_starting_balance
    casino_balance = casino_starting_balance
    bet_amount = 1
    # This payout multiplier creates the house edge.
    # For a fair game, it would be 2.0 (player wins $2 for a $1 bet on a 50/50 chance).
    # Here, 1.95 means the casino keeps a small percentage on average.
    payout_multiplier = 1.95 

    print(f"--- Simulating {num_rounds} rounds of a coin flip game ---")
    print(f"Player starts with: ${player_balance:.2f}")
    print(f"Casino starts with: ${casino_balance:.2f}\n")

    for i in range(num_rounds):
        # Player places a bet
        if player_balance < bet_amount:
            print(f"Player ran out of money after {i} rounds!")
            break
        player_balance -= bet_amount # Player bets $1
        casino_balance += bet_amount # Casino takes the bet

        # Simulate coin flip (50% chance for 'Heads', 50% for 'Tails')
        # We assume player always bets on 'Heads' for simplicity
        coin_flip = random.choice(['Heads', 'Tails'])

        if coin_flip == 'Heads':
            # Player wins: Casino pays out
            winnings = payout_multiplier * bet_amount
            player_balance += winnings
            casino_balance -= winnings
        # else (coin_flip == 'Tails'):
            # Player loses, casino keeps the bet. Balances already updated.

    print("\n--- Simulation Complete ---")
    print(f"Final Player Balance: ${player_balance:.2f}")
    print(f"Final Casino Balance: ${casino_balance:.2f}")
    print(f"Player Net Change: ${player_balance - player_starting_balance:.2f}")
    print(f"Casino Net Change: ${casino_balance - casino_starting_balance:.2f}")

    # Calculate and display the house edge effect
    total_bets = num_rounds * bet_amount
    casino_profit = casino_balance - casino_starting_balance
    if total_bets > 0:
        # The house edge is the casino's average profit as a percentage of total money wagered.
        effective_house_edge = (casino_profit / total_bets) * 100
        print(f"\nTotal money bet by player: ${total_bets:.2f}")
        print(f"Casino's effective profit percentage (House Edge): {effective_house_edge:.2f}%")
    else:
        print("No bets placed.")

if __name__ == "__main__":
    # Run a simulation with a large number of rounds to see the house edge in action.
    # The larger the number of rounds, the closer the effective house edge will be to its theoretical value.
    simulate_casino_game(num_rounds=100000, player_starting_balance=1000, casino_starting_balance=1000)
