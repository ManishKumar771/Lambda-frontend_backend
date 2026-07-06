import json

def lambda_handler(event, context):

    data = {
        "team1": "India",
        "team2": "Afghanistan",
        "score": "279/3",
        "overs": "64.5",
        "runrate": "4.32",
        "wickets": 3,
        "batsman1": "S. Gill 64* (81)",
        "batsman2": "R. Pant 3* (8)",
        "bowler1": "Z. Rahman 1/60 (13.5)",
        "bowler2": "A. Malik 0/12 (4.0)",
        "status": "IND chose to bat",
        "innings": "1st Innings"
    }

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(data)
    }
