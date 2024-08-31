def main():
    spacecraft = {"name": "Voyager 1"}
    spacecraft.update({"distace": 42.123, "orbit": "Sun"})
    print(create_report(spacecraft))


def create_report(spacecraft):
    return f"""
    ========= REPORT =========

    Name: {spacecraft.get('name', 'Unknown' )}
    Distace: {spacecraft.get('distace', 'Unknown')} AU
    Orbit: {spacecraft.get('orbit', 'Unknown')}

    ======= END REPORT =======
    """


main()
