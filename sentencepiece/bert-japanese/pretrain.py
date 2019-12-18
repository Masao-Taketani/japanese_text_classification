from glob import glob
import subprocess


def main():
	input_files = glob("data/wiki/*/*tfrecord")
	input_files = ','.join(file for file in input_files)
	print("number of tfrecords: ", len(input_files))
	subprocess.call(["python "
			 "src/run_pretraining.py "
			 "--input_file={} "
			 "--output_dir={} "
			 "--do_train=True "
			 "--do_eval=True "
			 "--max_seq_length=512 "
			 "--num_train_steps=1300000".format(
			 input_files, "model/pretrain")])


if __name__ == "__main__":
	main()
