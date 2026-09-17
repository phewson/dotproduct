def winner(match):
    """
    Determine the winner of a match.
    The match is represented as a tuple containing:
    (
        home_team,
        away_team,
        home_score,
        away_score
    )
    Return the name of the winning team.
    If the scores are equal, return 'Draw'.
    Parameters
    ----------
    match : tuple
    Returns
    -------
    str
    Examples
    --------
    >>> winner(('Exeter', 'Bath', 24, 18))
    'Exeter'
    >>> winner(('Exeter', 'Bath', 21, 21))
    'Draw'
    HINT: Consider using tuple unpacking
    """
    home_team, away_team, home_score, away_score = match
    if home_score > away_score:
        return home_team
    if away_score > home_score:
        return away_team
    return "Draw"


def average_score(scores):
    """
    Calculate the mean score from a list of scores.
    Parameters
    ----------
    scores : list[int]
    Returns
    -------
    float
    Examples
    --------
    >>> average_score([20, 30, 40])
    30.0
    HINT: do this without using a pre-written average or mean function
    """
    total = 0
    for score in scores:
        total += score
    return total / len(scores)


def highest_score(scores):
    """
    Find the highest value in a list of scores.
    Parameters
    ----------
    scores : list[int]
    Returns
    -------
    int
    Examples
    --------
    >>> highest_score([10, 25, 17])
    25
    HINT: Do this without using a pre-built max function
    """
    highest = scores[0]
    for score in scores:
        if score > highest:
            highest = score
    return highest


def team_win_percentage(team):
    """
    Calculate a team's win percentage.
    The team dictionary contains:
    {
        "name": str,
        "wins": int,
        "losses": int
    }
    Win percentage is:
        wins / (wins + losses) * 100
    Parameters
    ----------
    team : dict
    Returns
    -------
    float
    Examples
    --------
    >>> win_percentage(
    ...     {"name": "Exeter", "wins": 12, "losses": 3}
    ... )
    80.0
    """
    return 100 * team["wins"] / (team["wins"] + team["losses"])


def home_team_won(match):
    """
    Determine whether the home team won.
    The match dictionary contains:
    {
        "home_team": str,
        "away_team": str,
        "home_score": int,
        "away_score": int
    }
    Parameters
    ----------
    match : dict
    Returns
    -------
    bool
    Examples
    --------
    >>> home_team_won(
    ...     {
    ...         "home_team": "Exeter",
    ...         "away_team": "Bath",
    ...         "home_score": 24,
    ...         "away_score": 18,
    ...     }
    ... )
    True
    """
    home_team, _, _, _ = match
    return home_team == winner(match)


def total_points_for(matches):
    """
    Calculate the total points scored across a season.
    The season is represented as a list of dictionaries.
    Parameters
    ----------
    matches : list[dict]
    Returns
    -------
    int
    Examples
    --------
    >>> total_points_for(
    ...     [
    ...         {"points_for": 24},
    ...         {"points_for": 18},
    ...     ]
    ... )
    42
    """
    total = 0
    for match in matches:
        total += match["points_for"]
    return total


def count_wins(matches):
    """
    Count the number of matches won.
    A match is considered a win when
    points_for > points_against.
    Parameters
    ----------
    matches : list[dict]
    Returns
    -------
    int
    Examples
    --------
    >>> count_wins(
    ...     [
    ...         {
    ...             "points_for": 24,
    ...             "points_against": 18
    ...         },
    ...         {
    ...             "points_for": 10,
    ...             "points_against": 12
    ...         },
    ...     ]
    ... )
    1
    """
    wins = 0
    for match in matches:
        if match["points_for"] > match["points_against"]:
            wins += 1
    return wins


def win_percentage(matches, team_name):
    """
    Calculate the percentage of matches won by a team.
    The matches are represented as tuples:
    (
    home_team,
    away_team,
    home_score,
    away_score
    )
    Use the winner() function to determine
    the result of each match.
    Draws should not count as wins.
    Parameters
    ----------
    matches : list[tuple]
    A list of match results.
    team_name : str
    The team whose win percentage should
    be calculated.
    Returns
    -------
    float
    Percentage of matches won.
    Example
    -------
    >>> matches = [
    ... ('Exeter', 'Bath', 24, 18),
    ... ('Sale', 'Exeter', 15, 20),
    ... ('Exeter', 'Bristol', 10, 20),
    ... ]
    >>> win_percentage(matches, 'Exeter')
    66.66666666666667
    """
    wins = 0
    for match in matches:
        if winner(match) == team_name:
            wins += 1
    print(wins)
    return 100 * wins / len(matches)
