POST=$(curl -s -X POST http://127.0.0.1:5000/api/timeline_post -d 'name=Lucy&email=lwang5@villanova.edu&content=This post was made by a script.')
ID=$(echo $POST | jq '.id')
echo
echo "id of newly created post is $ID:"
echo
curl -s http://127.0.0.1:5000/api/timeline_post | jq '.'
echo
echo 'now deleting...'
echo
curl -s -X DELETE http://127.0.0.1:5000/api/timeline_post/$ID | jq '.'