if [$? -ne 3]
then
    echo "invalid number of arguments"
else
    mongoimport -d $1 -c $2 --type csv --file $3 --headerline