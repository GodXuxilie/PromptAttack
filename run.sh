CUDA_VISIBLE_DEVICES=1 python -u robustness_eval.py \
    --dataset SST-2\
    --API_base "http://luxinyayaya.turn.aiguoguo199.com/v1"\
    --API_key "sk-FN8RF5DiyaRXu7AGD03c1e62C0E5445994202379E89a57F2"\
    --tau_1 0.15\
    --tau_2 0.93275\
    --batch_size 32
