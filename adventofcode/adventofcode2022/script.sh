arg=""
newline=$'\n'
IFS=$'\n'
while read -r line
do
  arg="$arg$newline$line"
done < "$2"
$1 $arg
IFS=