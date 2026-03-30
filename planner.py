def generate_plan(subjects, days, difficulty):
    tasks = []

    # Step 1: Create task list with priority
    for i in range(len(subjects)):
        d = max(1, int(days[i]))
        diff = max(1, min(5, int(difficulty[i])))

        urgency = 1 / d
        priority = diff * 0.6 + urgency * 0.4

        tasks.append({
            "subject": subjects[i],
            "priority": priority,
            "days_left": d
        })

    # Step 2: Sort by priority
    tasks.sort(key=lambda x: x["priority"], reverse=True)

    total_days = max(int(d) for d in days)
    hours_per_day = 5

    schedule = []

    # Step 3: Generate day-wise plan
    for day in range(1, total_days + 1):
        day_plan = []
        remaining_hours = hours_per_day

        # Calculate total priority (for fair distribution)
        total_priority = sum(t["priority"] for t in tasks if t["days_left"] >= day)

        for task in tasks:
            if task["days_left"] >= day and remaining_hours > 0:
                # Distribute hours proportionally
                hrs = (task["priority"] / total_priority) * hours_per_day
                hrs = round(hrs, 1)

                # Prevent exceeding remaining hours
                hrs = min(hrs, remaining_hours)

                if hrs > 0:
                    day_plan.append({
                        "subject": task["subject"],
                        "hours": hrs
                    })

                remaining_hours -= hrs

        schedule.append({
            "day": day,
            "tasks": day_plan
        })

    return schedule