n = 6
output=f"grid_{n}.json"

constrainchoice = [ "indomain", 
                    "indomain_interval",
                    "indomain_max",
                    "indomain_median",
                    "indomain_middle",
                    "indomain_min",
                    "indomain_random",
                    "indomain_reverse_split",
                    "indomain_split",
                    "indomain_split_random",
                    "outdomain_max",
                    "outdomain_median",
                    "outdomain_min",
                    "outdomain_random" ]

varchoice = ["input_order", 
             "occurrence", 
             "first_fail", 
             "anti_first_fail", 
             "most_constrained",
             "dom_w_deg",
             "impact",
             "max_regret",
             "smallest",
             "largest"]

strategy = ["complete"]

template = '''
    {
        "name": "0_[[n]]x[[m]]_minizinc[[a]][[b]][[c]]",
        "target": "minizinc",
        "n": [[o]],
        "k": 1,
        "knight1": {
            "x": 1,
            "y": 1
        },
        "knight2": {
            "x": 4,
            "y": 4
        },
        "occ": [
            {
                "x": 1,
                "y": 4
            }
        ],
        "params": [
            { "solver": "gecode" },
            { "allsolutions": "--all-solutions" },
            { "timeout": "--solver-time-limit 20000" },
            { "mzn2fzn": "" },
            { "verbose": "-v" },
            { "varchoice": "[[varchoice]]" },
            { "constrainchoice": "[[constrainchoice]]" },
            { "strategy": "[[strategy]]" }
        ]
    },
'''

run = '[\n'
for v in varchoice:
    for c in constrainchoice:
        for s in strategy:
            run += template.replace("[[varchoice]]",v) \
                           .replace("[[constrainchoice]]",c)\
                           .replace("[[strategy]]",s)\
                           .replace("[[a]]",v)\
                           .replace("[[b]]",c)\
                           .replace("[[c]]",s)\
                           .replace("[[n]]",str(n))\
                           .replace("[[m]]",str(n))\
                           .replace("[[o]]",str(n))
run = run[:-2]
run += "\n]"

with open(output, 'w') as o:
    o.write(run)
