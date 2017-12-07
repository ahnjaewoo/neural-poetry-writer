# Utility Codes

1. 코드북
- 캐릭터-숫자 변환, 숫자-캐릭터 변환 담당
- 함수
	1. 생성자(midfile_dir)
		- 중간 생성물 디렉토리를 인자로 받아야 함
		- 생성 부산물은 해당 디렉토리에서 저장/로드 됨
	2. gather(character)
		- 문자 하나를 받아 dictionary에 임시로 저장
		- 모든 gather가 끝나면 반드시 sort_codes가 수행되어야 함
	3. sort_codes()
		- 임시로 저장된 문자들을 사용 빈도수 내림차순으로 정렬
		- 정렬 후 dictionary를 정렬결과로 갱신함
		- 이후 변환 함수 수행 가능
	4. save_to(filename)
		- dictionary 저장
	5. load_from(filename)
		- dictionary 로드
		- 이후 변환 함수 수행 가능
	6. get_number(text)
		- 문자열을 dictionary를 이용하여 정수 배열로 변환
		- ex) asdf => [0, 1, 2, 3]
	7. get_number_batch(batch)
		- 문자열의 배열을 정수 배열의 배열로 변환
		- get_number 함수 사용
	8. get_number_batchs(batchs)
		- 문자열 배치의 배열을 정수 배치의 배열로 변환
		- get_number_batch 사용
	9. get_string(number_text)
		- 정수 배열을 문자열로 변환
		- get_number 함수의 역변환
	10. get_string_batch(number_batch)
		- get_number_batch 함수의 역변환
	11. get_string_batchs(np_batchs)
		- get_number_batchs 함수의 역변환
	12. get_vectors(text)
		- deprecated
	13. size()
		- dictionary 길이를 반환
	13. debug_print()
		- debug purpose only

2. 데이터 게더러
- raw data 시 파일을 하나로 합침
- 시 파일과 제목 매핑 파일 생성

3. 배치 메이커
- 시 파일로 학습용 문자열 시퀀스와 배치 구성
- 제목 매핑 파일의 보조를 받음
- 처리 옵션 존재
	1. (drop/add) : 시퀀스 길이로 나누어질 때, 나머지 문자열을 버리는지, 초기 문자열 값으로 채우는지의 문제 (dropped/padded)
	2. (normal/stride) : 시퀀스 구성이 겹치는 스트라이드 방식을 사용하는지의 문제
	3. (whole/one) : 두 개 이상의 시가 섞이지 않도록 시퀀스를 구성하는지의 문제 (whole data text/separate each poem)

4. 데이터 로더
- 앞서 명시한 클래스의 기능을 이용하여 학습 전의 배치 생성까지의 작업에 관여

1. code_book
- manage character:number mapping, vector creation based on number code dictionary
- major functions are below:
	1. gather character mapping of unseen character
	2. save to file
	3. load from file
	4. get numpy vectors that correspond to given text
	5. get expected size of a vector
- TODO : upper case letter should be same value as lower case letter

2. data_loader
- manage poem input data
- major functions are below:
	1. data_preprocess
		- make char, vocab, tensor vector
		- code_book module used
	2. load from file
	3. save to file
	4. make batch
- TODO : make 2 batch method

3. data_gatherer
- gather separated poem data, save to one file
- major functions:
	1. clean target file
		- 2 files : all poem connected file / poem separated file
	2. gather all files, save to target file
		- 2 files : all poem connected file / poem separated file
		- use data_parser
	3. parsing for poem files, before gather function

4. batch maker
- manage sequence and batch creation
- (drop/add), (normal/stride), (whole/one) mode
	1. (drop/add) : divided by seq_len, leftover part should be (dropped/padded)
	2. (normal/stride) : making sequence by striding seq_len filter
	3. (whole/one) : make sequence with (whole data text/separate each poem)