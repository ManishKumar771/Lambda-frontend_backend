def lambda_handler(event, context):

    html = """
<!DOCTYPE html>
<html>

<head>

<title>Cricket Dashboard</title>

<style>

body{
background:#0f172a;
font-family:Arial;
color:white;
margin:0;
padding:40px;
}

.card{
max-width:900px;
margin:auto;
background:#1e293b;
padding:30px;
border-radius:20px;
}

.score{
font-size:70px;
font-weight:bold;
color:#22c55e;
}

.row{
display:flex;
gap:20px;
margin-top:25px;
}

.box{
flex:1;
background:#334155;
padding:20px;
border-radius:12px;
text-align:center;
}

h2{
margin-top:35px;
}

</style>

</head>

<body>

<div class="card">

<h1 id="match">Loading...</h1>

<div class="score" id="score"></div>

<div class="row">

<div class="box">

<h3>Overs</h3>

<p id="overs"></p>

</div>

<div class="box">

<h3>Run Rate</h3>

<p id="runrate"></p>

</div>

<div class="box">

<h3>Wickets</h3>

<p id="wickets"></p>

</div>

</div>

<h2>Top Batsmen</h2>

<p id="bat1"></p>

<p id="bat2"></p>

<h2>Bowling</h2>

<p id="bowl1"></p>

<p id="bowl2"></p>

</div>

<script>

fetch("YOUR_BACKEND_FUNCTION_URL")

.then(response=>response.json())

.then(res=>{

const d=JSON.parse(res.body);

document.getElementById("match").innerHTML=d.team1+" vs "+d.team2;

document.getElementById("score").innerHTML=d.score;

document.getElementById("overs").innerHTML=d.overs;

document.getElementById("runrate").innerHTML=d.runrate;

document.getElementById("wickets").innerHTML=d.wickets;

document.getElementById("bat1").innerHTML=d.batsman1;

document.getElementById("bat2").innerHTML=d.batsman2;

document.getElementById("bowl1").innerHTML=d.bowler1;

document.getElementById("bowl2").innerHTML=d.bowler2;

})

.catch(err=>{

document.getElementById("match").innerHTML="Backend Not Reachable";

console.log(err);

});

</script>

</body>

</html>
"""

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/html"
        },
        "body": html
    }
