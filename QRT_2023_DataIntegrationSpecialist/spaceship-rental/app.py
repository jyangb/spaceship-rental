import json
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/spaceship/optimize', methods=['POST'])
def optimize_spaceship():
    contracts = json.loads(request.data)
    n = len(contracts)
    dp = [0] * (n + 1)
    path = [[] for _ in range(n + 1)]

    for i in range(n):
        # find the latest non-conflicting contract
        j = i
        while j > 0 and contracts[j - 1]['start'] + contracts[j - 1]['duration'] > contracts[i]['start']:
            j -= 1

        # calculate the new profit if we take this contract
        new_profit = dp[j] + contracts[i]['price']

        # update the DP table and path if the new profit is greater
        if new_profit > dp[i]:
            dp[i + 1] = new_profit
            path[i + 1] = path[j] + [contracts[i]['name']]
        else:
            dp[i + 1] = dp[i]
            path[i + 1] = path[i]

    return jsonify({'income': dp[n], 'path': path[n]})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
