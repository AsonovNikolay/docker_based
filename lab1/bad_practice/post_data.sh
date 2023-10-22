curl --request POST \
  --url http://localhost:1111/add_data \
  --header 'Content-Type: application/json' \
  --data '{
    "column1": $1,
    "column2": $2,
    "column3": $3
}
'
