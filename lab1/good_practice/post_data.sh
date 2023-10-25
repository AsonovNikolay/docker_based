#!/bin/bash
#!/bin/bash

if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <integer_value> <string_value> <string_value>"
    exit 1
fi

integer_value=$1
string_value1=$2
string_value2=$3

curl --request POST \
  --url http://localhost:1111/add_data \
  --header 'Content-Type: application/json' \
  --data "{
    \"column1\": $integer_value,
    \"column2\": \"$string_value1\",
    \"column3\": \"$string_value2\"
}"
