for file in 4*; do
    cp "$file" "${file/4/5}"
done
