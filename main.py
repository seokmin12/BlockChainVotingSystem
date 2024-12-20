import json
import rsa
from VotingModel.VotingSystem import VotingSystem

public_key, private_key = rsa.newkeys(1024)

voting_system = VotingSystem()


def init() -> dict:
    with open('./voters.json', 'r') as file:
        voters = json.load(file)
    return voters


def get_pw(voter) -> str:
    print(f"\n현재 투표자는 {voter['name']}입니다.")
    pw = input("투표자의 비밀번호를 입력하세요 : ")
    return pw


def check_pw(voter, pw_input):
    if pw_input != voter["password"]:
        print("비밀번호가 일치하지 않습니다. 다시 입력하세요.")
        pw = get_pw(voter)
        check_pw(voter, pw)
    else:
        act_result = act()


def act():
    print("1. 투표하기 | 2. 체인 확인 | 3. 결과 계산 | 4. 종료")
    result = int(input("번호를 입력하세요 : "))
    return result


def voting(voter_id):
    print("\n투표를 진행합니다.")
    print('-' * 50)
    print(voting_system.get_candidates())
    print('-' * 50)
    selected_candidate = input("투표를 원하시는 후보를 입력하세요 : ")
    voting_system.cast_vote(voter_id=str(voter_id), candidate=selected_candidate, private_key=private_key,
                            public_key=public_key)


def get_chain():
    print("\n체인을 확인합니다.")
    chains = voting_system.get_chain()
    for chain in chains:
        print(chain.__dict__)


def get_results():
    print("\n투표 결과를 확인합니다.")
    print(voting_system.calculate_results())


try:
    voters = init()
    for voter in voters:
        pw = get_pw(voter)
        check_pw(voter, pw)
        # act_result = act()
        # if act_result == 1:
        #     voting(voter['id'])
        # elif act_result == 2:
        #     get_chain()
        # elif act_result == 3:
        #     get_results()
        # elif act_result == 4:
        #     break

except KeyboardInterrupt:
    print("종료")
