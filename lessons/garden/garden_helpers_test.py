"""Test my garden functions."""

__author__ = "730373934"

by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
print(by_kind)

new_plant: str = "elderberry"
new_plant_kind: str = "fruit"

# Function name: add_by_kind
# Parameters: dict[str, list[str]], str, str
# Return Type: None


def add_by_kind(by_kind: dict[str, list[str]], new_plant_kind: str, new_plant: str) -> None:
    """Add plant under its kind."""
    if new_plant_kind in by_kind:  # if the kind is already in the dictionary ("flower" was in by_kind, so I did this)
        by_kind[new_plant_kind].append(new_plant)
    else:  # if the kind is not in the dictionary (ex: "fruit" is not in by_kind)
        by_kind[new_plant_kind] = []
        by_kind[new_plant_kind].append(new_plant)


def add_by_date(garden_by_date: dict[str, list[str]], month: str, plant: str) -> None:
    """Add plant under date to sow seeds."""
    if month in garden_by_date:
        garden_by_date[month].append(plant)
    else:
        garden_by_date[month] = []
        garden_by_date[month].append(plant)


# Function name: lookup_by_kind_and_date
# Parameters: dict[str, list[str]], dict[str, list[str]], str, str
# Return Type: str
def lookup_by_kind_and_date(plants_by_kind: dict[str, list[str]], plants_by_date: dict[str, list[str]], kind: str, month: str) -> str:
    """Return string with list of plants of a specific kind to plant in a specific month."""
    assert kind in plants_by_kind
    assert month in plants_by_date
    # Get a list of all plants of the specific kind input
    kind_list: list[str] = plants_by_kind[kind]
    # Get a list of all plants planted in a specific month
    month_list: list[str] = plants_by_date[month]
    # Go through both lists and find elements that appear in both.
    # kind_list = ["marigold", "daisy"]
    # month_list = ["daisy", "rose"]
    combined_list: list[str] = []
    for plant in kind_list:
        for other_plant in month_list:
            if plant == other_plant:  # plant is in both kind_list and month_list
                combined_list.append(other_plant)
    # "<kind>s to plant in <month>: <combined_list>"
    if len(combined_list) > 0:
        return f"{kind}s to plant in {month}: {combined_list}"
    else:  # "No <kind>s to plant in <month>."
        return f"No {kind}s to plant in {month}."


# Part 1: add_by_kind unit test
def test_add_by_kind_with_existing_kind() -> None:
    """Test adding a new plant to an existing kind in the dictionary, should add the new plant to the existing list of that kind."""
    by_kind = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
    add_by_kind(by_kind, "flower", "daisy")
    assert "daisy" in by_kind["flower"]


# edge case test 1
def test_add_by_kind_with_new_kind() -> None:
    """Test adding a new plant under a new kind in the dictionary, should create a new list for that kind and add the new plant to it."""
    by_kind = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
    add_by_kind(by_kind, "fruit", "apple")
    assert "apple" in by_kind["fruit"]


# Part 2: add_by_date test
def test_add_by_date_with_existing_month() -> None:
    """Test adding a new plant to an existing month in the dictionary, should add the new plant to the existing list for that month."""
    garden_by_date = {"March": ["tomatoes"], "April": ["lettuce"]}
    add_by_date(garden_by_date, "March", "peppers")
    assert "peppers" in garden_by_date["March"]


# edge case test 2
def test_add_by_date_with_new_month() -> None:
    """Test adding a new plant under a new month in the dictionary, should create a new list for that month and add the new plant to it."""
    garden_by_date = {"March": ["tomatoes"], "April": ["lettuce"]}
    add_by_date(garden_by_date, "May", "beans")
    assert "beans" in garden_by_date["May"]


# Part 3: lookup_by_kind_and_date test
def test_lookup_by_kind_and_date_with_valid_entries() -> None:
    """Test looking up plants by kind and date where both exist in the dictionary, should return a string with the plants that are of the specified kind and are planted in the specified month."""
    plants_by_kind = {"flower": ["daisy", "rose"], "vegetable": ["carrot"]}
    plants_by_date = {"March": ["daisy", "carrot"]}
    result = lookup_by_kind_and_date(plants_by_kind, plants_by_date, "flower", "March")
    assert result == "flowers to plant in March: ['daisy']"


# edge case test 3
def test_lookup_by_kind_and_date_with_no_matching_plants() -> None:
    """Test looking up plants by kind and date where there are no matching plants, should return a string indicating no plants of that kind to plant in that month."""
    plants_by_kind = {"flower": ["daisy", "rose"], "vegetable": ["carrot"]}
    plants_by_date = {"March": ["carrot"]}
    result = lookup_by_kind_and_date(plants_by_kind, plants_by_date, "flower", "March")
    assert result == "No flowers to plant in March."