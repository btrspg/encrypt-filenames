# Encrypt filenames

Sometimes, we may name our file in a certain way so that we could easily find the file or a group of files. For example, if I have several fastq files, and I named them in a quite regular way like "sampleName_sampleTissue_sampleAge_sampleGender_R1.fq.gz". I could use  `ls` to get all that `sampleName` files or all that `sampleTissue` files.



It is a very good way to name files, however, when we send the files to others, it would be easy to leak information. So I just want to write a package to encrypt the fillenames as changing 'sampleName_sampleTissue_sampleAge_sampleGender_R1.fq.gz'  to ''abd54ed96011c648e7e012dfef1a9f3174b70c86de55d0840f2a576d.fq.gz'', so that others will know nothing from the filename.



## Run

```bash
encryptfn.py \
	-f sampel1_group1_family2_type3.fq.gz  \
			sampel1_group1_family5_type3.fq.gz  \
			sampel1_group1_family2_type3.fq.gz  \
			sampel1_group1_family2_type6.fq.gz  \
			sampel6_group4_family2_type3.fq.gz  \
   -in Sample Group Family Type  \
   -o /tmp/test
```



## Result

```bash
ls -lthr /tmp/test 
#-rw-r--r--  1 logan  wheel   549B Mar 13 21:19 information.csv
#-rw-r--r--  1 logan  wheel   607B Mar 13 21:19 cp.bash

```

### cp.bash

```bash
#! /bin/bash
cp sampel1_group1_family2_type3.fq.gz /tmp/test/12b5f9da8dee6e265f1c3361b01f72fada4bf49b226c882deae9d54b47480f14.fq.gz
cp sampel1_group1_family5_type3.fq.gz /tmp/test/981d15ee64749220f83457a9b45a8e943fb75ce02f77220a4c152f0eea2c313b.fq.gz
cp sampel1_group1_family2_type3.fq.gz /tmp/test/12b5f9da8dee6e265f1c3361b01f72fada4bf49b226c882deae9d54b47480f14.fq.gz
cp sampel1_group1_family2_type6.fq.gz /tmp/test/71b37ab88cf06cd028489bbcb782891bf8cedc3b16ca5995b4bed52e09cd06a2.fq.gz
cp sampel6_group4_family2_type3.fq.gz /tmp/test/a88c4d4e59fc6236a1986fd8231c6bbc6edbbcc598894a3e4b4541cb87c1bafd.fq.gz
```

### information.csv

|      | Family  | Group  | Sample  | Type  | encrypt_file                                                 |
| ---- | ------- | ------ | ------- | ----- | ------------------------------------------------------------ |
| 0    | family2 | group1 | sampel1 | type3 | 12b5f9da8dee6e265f1c3361b01f72fada4bf49b226c882deae9d54b47480f14.fq.gz |
| 1    | family5 | group1 | sampel1 | type3 | 981d15ee64749220f83457a9b45a8e943fb75ce02f77220a4c152f0eea2c313b.fq.gz |
| 2    | family2 | group1 | sampel1 | type3 | 12b5f9da8dee6e265f1c3361b01f72fada4bf49b226c882deae9d54b47480f14.fq.gz |
| 3    | family2 | group1 | sampel1 | type6 | 71b37ab88cf06cd028489bbcb782891bf8cedc3b16ca5995b4bed52e09cd06a2.fq.gz |
| 4    | family2 | group4 | sampel6 | type3 | a88c4d4e59fc6236a1986fd8231c6bbc6edbbcc598894a3e4b4541cb87c1bafd.fq.gz |