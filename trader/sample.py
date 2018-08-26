import re
from itertools import permutations
from typing import Dict

from collections import defaultdict

DATA = """
Crown = 3.9836847299331017 Mariborian crown
Crown = 1.3654159689098424 Ducat
Crown = 0.9955943404476554 Bizant
Crown = 2.7222403605224907 Farthing
Crown = 1.6474336517887584 Floren
Crown = 4.0452567636790375 Lintar
Crown = 2.7922344718970336 Mark Silver
Crown = 4.678984909839266 Noble
Crown = 3.8764957363113473 Oren
Crown = 3.9794806508820217 Thaler
Crown = 1.4898127670285535 Denar
Mariborian crown = 0.24108333492950082 Crown
Mariborian crown = 0.3358969748477351 Ducat
Mariborian crown = 0.2449195957469975 Bizant
Mariborian crown = 0.669680392443315 Farthing
Mariborian crown = 0.39323643450328705 Floren
Mariborian crown = 0.9951469298304716 Lintar
Mariborian crown = 0.6868991820306637 Mark Silver
Mariborian crown = 1.1510462103559793 Noble
Mariborian crown = 0.9536311428060514 Oren
Mariborian crown = 0.9789657822469985 Thaler
Mariborian crown = 0.36649901050590933 Denar
Ducat = 0.703375397584364 Crown
Ducat = 2.859210031395363 Mariborian crown
Ducat = 0.7145679235154208 Bizant
Ducat = 1.9538335672476626 Farthing
Ducat = 1.147291385961167 Floren
Ducat = 2.903402127024062 Lintar
Ducat = 2.004070440631982 Mark Silver
Ducat = 3.358247827805544 Noble
Ducat = 2.7822772752674343 Oren
Ducat = 2.8561926377483937 Thaler
Ducat = 1.0692833136071125 Denar
Bizant = 0.9646499191308875 Crown
Bizant = 3.9212868903805282 Mariborian crown
Bizant = 1.3440289836621446 Ducat
Bizant = 2.679600962890672 Farthing
Bizant = 1.5734621177935926 Floren
Bizant = 3.9818944999455708 Lintar
Bizant = 2.74849873215301 Mark Silver
Bizant = 4.6056963417256025 Noble
Bizant = 3.8157768352489496 Oren
Bizant = 3.917148661281912 Thaler
Bizant = 1.466477311463528 Denar
Farthing = 0.35279764929194807 Crown
Farthing = 1.4341169471843136 Mariborian crown
Farthing = 0.4915464736092654 Ducat
Farthing = 0.3584115744472452 Bizant
Farthing = 0.5754561581341819 Floren
Farthing = 1.4562827316411409 Lintar
Farthing = 1.0051977122012423 Mark Silver
Farthing = 1.6844233441467251 Noble
Farthing = 1.3955291665927578 Oren
Farthing = 1.4326034888101724 Thaler
Farthing = 0.53632902254368 Denar
Floren = 0.6008132703403808 Crown
Floren = 2.4422965822409624 Mariborian crown
Floren = 0.8371020751588796 Ducat
Floren = 0.6103737669558471 Bizant
Floren = 1.6689368710796884 Farthing
Floren = 2.4800448424005586 Lintar
Floren = 1.711848494507758 Mark Silver
Floren = 2.9563808702721355 Noble
Floren = 2.3765817150956763 Oren
Floren = 2.4397191674619334 Thaler
Floren = 0.9133666130135479 Denar
Lintar = 0.2374138543251691 Crown
Lintar = 0.9650836185201407 Mariborian crown
Lintar = 0.330784355036756 Ducat
Lintar = 0.24119172419388005 Bizant
Lintar = 0.6594873228481453 Farthing
Lintar = 0.3872510623922353 Floren
Lintar = 0.6764440287272222 Mark Silver
Lintar = 1.1335263691573916 Noble
Lintar = 0.9391161163599605 Oren
Lintar = 0.9640651423860545 Thaler
Lintar = 0.36092060330927966 Denar
Mark Silver = 0.343953922804881 Crown
Mark Silver = 1.3981673368146872 Mariborian crown
Mark Silver = 0.4792246722111916 Ducat
Mark Silver = 0.349427121346234 Bizant
Mark Silver = 0.955433929407637 Farthing
Mark Silver = 0.5610309575183305 Floren
Mark Silver = 1.4197774822656966 Lintar
Mark Silver = 1.6421991984531203 Noble
Mark Silver = 1.360546852286412 Oren
Mark Silver = 1.3966918169357068 Thaler
Mark Silver = 0.5228846382288421 Denar
Noble = 0.21154160978775244 Crown
Noble = 0.8343713669870656 Mariborian crown
Noble = 0.28598246741890276 Ducat
Noble = 0.20852438561769573 Bizant
Noble = 0.570165453558534 Farthing
Noble = 0.3348012463322727 Floren
Noble = 0.847267453260849 Lintar
Noble = 0.5848255198910429 Mark Silver
Noble = 0.8119209390046149 Oren
Noble = 0.8334908346601939 Thaler
Noble = 0.3120370208114515 Denar
Oren = 0.24774953084660475 Crown
Oren = 1.0070979825323565 Mariborian crown
Oren = 0.3451848629672201 Ducat
Oren = 0.2516918681218791 Bizant
Oren = 0.6881977267052443 Farthing
Oren = 0.404109816169875 Floren
Oren = 1.0226637401587104 Lintar
Oren = 0.7058926330879666 Mark Silver
Oren = 1.182873792092879 Noble
Oren = 1.0060351676215942 Thaler
Oren = 0.37663307559245535 Denar
Thaler = 0.241338024796561 Crown
Thaler = 0.981035310341098 Mariborian crown
Thaler = 0.3362518295534529 Ducat
Thaler = 0.24517833839007352 Bizant
Thaler = 0.6703878690101795 Farthing
Thaler = 0.3936518648575093 Floren
Thaler = 0.9961982419808445 Lintar
Thaler = 0.6876248492005088 Mark Silver
Thaler = 1.152262220605636 Noble
Thaler = 0.9546385960547661 Oren
Thaler = 0.36688619439935727 Denar
Denar = 0.6446447642649267 Crown
Denar = 2.620470922075013 Mariborian crown
Denar = 0.898171689185155 Ducat
Denar = 0.6549027335728306 Bizant
Denar = 1.7906918321239693 Farthing
Denar = 1.0514945327717542 Floren
Denar = 2.6609730538907894 Lintar
Denar = 1.8367340131719034 Mark Silver
Denar = 3.0778399226555946 Noble
Denar = 2.549961918477982 Oren
Denar = 2.61770547559661 Thaler
"""
PATTERN = r'([\w ]+) = (\d\.\d+) ([\w ]+)'


def parse_data(data: str) -> Dict[str, Dict[str, float]]:
    rates: Dict[str, Dict[str, float]] = defaultdict(dict)

    for line in data.strip().split('\n'):
        match = re.match(PATTERN, line).groups()
        first_currency, rate, second_currency = match
        rates[first_currency][second_currency] = float(rate)

    return rates


def filter_solutions(solutions):
    """Make sure the solution is correct:

    A -> B, B -> A is ok
    A -> B, D -> C is not
    A -> B, B -> C is not
    """
    filtered = []
    for solution in solutions:
        ok = True
        start_currency = solution[0][0]
        last_currency = solution[0][1]
        for step in solution[1:]:
            if step[0] != last_currency:
                ok = False
                break
            last_currency = step[1]

        # Last step should return to the initial point
        if step[1] != start_currency:
            ok = False
        if ok:
            filtered.append(solution)
    return filtered


def main():
    rates = parse_data(DATA)
    anomalies = []

    for first_currency in rates.keys():
        for second_currency, rate in rates[first_currency].items():
            exchange = rate*rates[second_currency][first_currency]
            if exchange > 0.961:
                anomalies.append((first_currency, second_currency, exchange))

    for solution in filter_solutions(permutations(anomalies, 3)):
        print([(first, second) for first, second, _ in solution])


if __name__ == '__main__':
    main()

# answer = [("Crown", "Floren"), ("Floren", "Noble"), ("Noble", "Crown")]
