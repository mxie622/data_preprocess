# n=0;while(($n<=10));do top -n 1;n=$((n + 1));sleep 2;done
set -ex
python ./python/exec/main.py --image_dim_x 256 --image_dim_y 256