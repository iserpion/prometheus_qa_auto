

class SpaceXData:

    history_id = "5f6fb312dcfdf403df379720"
    rocket_id = "5e9d0d95eda69973a809d1ec"
    error_text = "GRAPHQL_VALIDATION_FAILED"

    company_data = {
        "data": {
            "company": {
                "name": "SpaceX",
                "ceo": "Elon Musk",
                "coo": "Gwynne Shotwell",
                "cto": "Elon Musk",
                "cto_propulsion": "Tom Mueller",
                "founder": "Elon Musk",
                "employees": 9500,
                "founded": 2002,
                "launch_sites": 3,
                "test_sites": 3,
                "valuation": 74000000000,
                "vehicles": 4,
                "headquarters": {
                    "address": "Rocket Road",
                    "city": "Hawthorne",
                    "state": "California",
                },
            }
        }
    }

    history_data = {
        "data": {
            "history": {
                "id": "5f6fb312dcfdf403df379720",
                "title": "First successfull Dragon launch",
                "details": "SpaceX becomes the first private company to successfully launch, orbit, and recover a spacecraft.",
                "event_date_unix": 1275677100,
                "event_date_utc": "2010-06-04T18:45:00Z",
            }
        }
    }

    rocket_data = {
        "data": {
            "rocket": {
                "id": "5e9d0d95eda69973a809d1ec",
                "name": "Falcon 9",
                "type": "rocket",
                "active": True,
                "company": "SpaceX",
                "country": "United States",
                "description": "Falcon 9 is a two-stage rocket designed and manufactured by SpaceX for the reliable and safe transport of satellites and the Dragon spacecraft into orbit.",
                "first_flight": "2010-06-04",
                "cost_per_launch": 50000000,
                "stages": 2,
                "boosters": 0,
                "success_rate_pct": 98,
                "wikipedia": "https://en.wikipedia.org/wiki/Falcon_9"
            }
        }
    }
