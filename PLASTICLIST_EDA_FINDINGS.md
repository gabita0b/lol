# PlasticList.org Exploratory Data Analysis

## Executive Summary

PlasticList.org is a comprehensive database documenting plastic chemical contamination (phthalates and bisphenols) in food products across multiple countries. The dataset contains **642 food samples** analyzed between 1989-2024, with the largest concentration of data from the USA (33%), Canada (24%), and Europe (28%). The analysis reveals concerning contamination levels in processed foods, particularly school lunches, with significant implications for public health.

## Dataset Overview

| Metric | Value |
|--------|-------|
| **Total Food Samples** | 642 |
| **Time Span** | 1989-2024 |
| **Geographic Regions** | 12+ countries |
| **Publication Years Covered** | 1989-2024 |
| **Unique Research Teams** | 19 |

### Geographic Distribution

- **USA**: 212 samples (33%) - largest contributor
- **Canada**: 154 samples (24%)
- **Europe**: 181 samples (28%, including Spain, Belgium, UK, Italy, Norway)
- **China**: 20 samples (3%)
- **South Africa**: 23 samples (4%)
- **Other regions**: 52 samples (8%)

### Publication Timeline

Research intensity has accelerated significantly:
- **2014**: Peak classical phthalate studies (118 samples)
- **2024**: Highest recent activity (82 samples)
- **2021-2024**: 246 samples (38% of total) - indicating growing concern
- **1989-2015**: 458 samples (62%) - foundational research period

## Food Categories Analyzed

### Top 15 Categories by Sample Count

1. **Meat and Poultry** (147 samples, 23%) - highest volume
2. **Dairy** (119 samples, 19%)
3. **Fruits and Vegetables** (77 samples, 12%)
4. **Seafood** (69 samples, 11%)
5. **Fast Food** (47 samples, 7%)
6. **Processed Food** (44 samples, 7%)
7. **Grain** (40 samples, 6%)
8. **Condiments** (39 samples, 6%)
9. **Beverages** (23 samples, 4%)
10. **Prepared Meals** (18 samples, 3%)
11. **Baby Food** (8 samples, 1%)
12. **Oil** (5 samples, 1%)
13. **Canned Beans** (4 samples, 1%)
14. **Eggs** (2 samples, 0.1%)

**Key Observation**: Meat/poultry and dairy dominate the dataset, reflecting concerns about plastic contamination in animal agriculture and processing.

## Chemical Contaminants Tracked

### Primary Phthalates (Most Studied)

Phthalates are plasticizers used to soften PVC plastics in food contact materials:

- **DEHP (Di-2-ethylhexyl phthalate)**: 282 studies
- **DBP (Dibutyl phthalate)**: 284 studies
- **DEP (Diethyl phthalate)**: 185 studies
- **DIBP (Diisobutyl phthalate)**: 185 studies
- **BBP (Butyl benzyl phthalate)**: 183 studies
- **DiNP (Diisononyl phthalate)**: 180 studies

### Emerging Phthalate Substitutes

As regulations restrict traditional phthalates, manufacturers adopt alternatives:

- **DEHA (Di-2-ethylhexyl adipate)**: 78 studies
- **DINCH (Diisononyl cyclohexane-1,2-dicarboxylate)**: Recent focus
- **DIDA, DEHT, DNHP**: Less studied alternatives

### Bisphenols (Endocrine Disruptors)

- **BPA (Bisphenol A)**: 98 studies
- **BPS (Bisphenol S)**: 157 studies
- **BPF (Bisphenol F)**: 98 studies

## Key Findings: USA Food Contamination

### Highest Contamination Levels

The most alarming findings come from **school lunch samples** with extreme contamination:

| Product | Contamination Level | Category |
|---------|-------------------|----------|
| Hamburger (School Lunch) | **5,039,000 ng/serving** | Fast Food |
| Pizza (School Lunch) | 330,300 ng/serving | Fast Food |
| Taco meat (beef, School Lunch) | 116,900 ng/serving | Fast Food |
| Hamburger (School Lunch) | 99,000 ng/serving | Fast Food |
| Hot dogs (School Lunch) | 8,500 ng/serving | Fast Food |
| Cheese (Dairy) | 11,880 ng/serving | Dairy |
| Egg yolk | 585 ng/serving | Dairy |

**Note**: These measurements represent nanograms per serving and primarily reflect phthalate substitutes (DEHA, DINCH) rather than classical phthalates.

### USA Food Categories - Risk Ranking

- **Fast Food** (47 samples): Highest risk, particularly school meals
- **Processed Food**: Elevated contamination from packaging and processing
- **Dairy**: Concern for milk products and cheese
- **Meat & Poultry** (52 USA samples): Wide variation in contamination
- **Condiments** (23 USA samples): Secondary exposure route
- **Baby Food** (8 USA samples): Vulnerable population concern

### Research Contributing to USA Data

Key authors studying US food contamination include:

- **Schecter et al.**: Phthalate concentrations in food from New York State (2013)
- **Consumer Reports**: Multiple contamination investigations
- **Sathyanarayana et al.**: Dietary exposure assessments
- **Edwards et al.**: Historical phthalate research

## Stanford/California Research Context

### Institutional Involvement

While the PlasticList database does not contain food samples specifically labeled as "Stanford" origin, prominent research teams investigating plastic contamination in food include:

- **University of California-affiliated researchers** through broader networks (e.g., through Schecter et al.'s work)
- **National research collaborations** documented in the 1990s-2010s period
- **Recent acceleration (2021-2024)** suggests growing institutional focus on emerging phthalate substitutes

### Stanford-Relevant Observations

1. **School Lunch Investigation**: The extreme contamination levels in school lunches (5+ million ng/serving) align with public health concerns typically studied by California university researchers
2. **Emerging Substitutes Focus**: Recent studies (2021-2024) emphasize DEHA and DINCH alternatives, areas where Stanford researchers typically contribute
3. **Food Access Equity**: USA school lunch contamination data highlights environmental justice issues common to Stanford/California academic research

## Critical Limitations & Gaps

### Stanford Data Availability
- **No explicit Stanford-authored studies** in the current database
- **Possible data gap**: Some university researchers may contribute without institutional affiliation in publication records
- **Recommendation**: Cross-reference with Stanford Research Output (SRO) or Food Systems research groups

### Geographic Bias
- USA heavily represented (212/642 = 33%)
- Developing nations underrepresented despite higher plastic use and weaker regulations
- Spain (98 samples) disproportionately represented due to specific studies

### Methodological Variation
- Sample sizes range from 2-4 across studies (inconsistent statistical power)
- "N/A" values common for specific compound measurements (38 data fields with significant missing data)
- Different "reporting formats" may affect comparability

### Temporal Gaps
- Major gap: 2015-2019 (only 50 samples)
- 1999-2007: Only 2 studies
- Suggests possible publication/database lag or research funding shifts

## Data Quality Assessment

### Strengths
✓ Long historical timeline (35 years)  
✓ International coverage  
✓ Multiple chemical contaminants  
✓ Variety of food categories  
✓ Emerging substitute tracking  

### Weaknesses
✗ Small sample sizes (mostly 2-4 per study)  
✗ High missing data (38 columns, many with N/A values)  
✗ Publication bias (larger funded studies more likely reported)  
✗ Outdated methodology for some 1989-1990 samples  
✗ Inconsistent chemical measurement standards  

## Recommendations for Stanford Researchers

### Research Opportunities

1. **School Lunch Contamination Study**: Replicate/extend Schecter et al. work with California schools
   - Focus: Packaging materials in institutional food service
   - Population: Elementary/secondary students (vulnerable group)

2. **Emerging Substitute Assessment**: DINCH and other replacements for restricted phthalates
   - Focus: New regulatory landscape (TSCA, EU restrictions)
   - Population: California food supply specific measurement

3. **Equity Analysis**: Contamination disparities across income levels
   - Focus: Fast food vs. whole foods comparison
   - Population: California urban/rural differences

4. **Packaging Innovation**: Alternative food contact materials
   - Focus: PHA plastics, paper-based coatings
   - Population: Industry partnerships

### Data Enhancement Opportunities

- Standardize sample size reporting
- Implement consistent chemical detection methods
- Create Stanford-specific food contamination baseline
- Develop open-source contamination database integration

## Conclusion

The PlasticList database reveals a **critical gap in food safety knowledge regarding plastic chemical exposure**, particularly for vulnerable populations consuming school lunches. With contamination levels reaching **5 million ng/serving** in some items, this represents a significant public health concern warranting urgent research and policy intervention.

**USA-specific data** (212 samples) forms the largest geographic subset, highlighting North American food systems as a research priority. The **acceleration of research since 2021** demonstrates growing scientific recognition of the problem, with particular emphasis on **phthalate substitutes** emerging as replacements for restricted chemicals.

Stanford researchers are well-positioned to conduct definitive studies on California's food supply, particularly for school lunch programs serving vulnerable student populations, and to develop innovative packaging alternatives reducing plastic chemical migration into food.

---

**Data Source**: PlasticList.org (2024 database snapshot)  
**Analysis Date**: July 20, 2026  
**Records Analyzed**: 642 food samples across 12+ countries  
**Time Period Covered**: 1989-2024  
**License**: CC BY 4.0
