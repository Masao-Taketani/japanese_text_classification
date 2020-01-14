import subprocess

PRETRAINED_MODEL_PATH = "model/pretrain/model.ckpt-1300000"
OUTPUT_DIR = "model/livedoor_output"

def main():
	print("Start finetuning")
	cmd = "python src/run_classifier.py --task_name=livedoor --do_train=true \
	       --do_eval=True --data_dir=data/livedoor --model_file=model/spm.model \
	       --vocab_file=model/spm.vocab --init_checkpoint={} --max_seq_length=512 \
	       --train_batch_size=4 --learning_rate=2e-5 --num_train_epochs=10 \
	       --output_dir={}".format(PRETRAINED_MODEL_PATH, OUTPUT_DIR)

	subprocess.call(cmd.split())
	print("End finetuning")


if __name__ == "__main__":
	main()
