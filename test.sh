
min=1
max=11

for x in $(seq $min $max); do
    prog="./cp${x}.py";
    echo ">>>    running $prog    >>>";
    $prog ;
    echo "<<<  done running $prog <<<";
    #echo;
done
