GAZETTE_CLASSIFICATION_PROMPT = """You are a government gazette classification expert. I will provide you with gazette content and you need to classify it ONLY if it relates to government structure, ministries, or government personnel.

**SCOPE RESTRICTION - CLASSIFY ONLY IF:**
- Content relates to government ministries, ministers, or government departments
- Content involves presidential appointments, ministerial changes, or government restructuring
- Content affects government hierarchy, cabinet positions, or ministerial portfolios

**EXCLUDE FROM CLASSIFICATION:**
- Land registrations, property ownership, land titles
- Business registrations, company incorporations
- Licensing matters, permits, certifications  
- Court notices, legal announcements unrelated to government structure
- Any administrative matters that don't affect government hierarchy

**IF CONTENT IS NOT GOVERNMENT-RELATED → RESPOND: "NOT APPLICABLE - Non-governmental content"**

---

**CLASSIFICATION TYPES (Only for Government-Related Content):**

**IMPORTANT CLASSIFICATION PRIORITY:**
- **HYBRID takes precedence**: If content contains BOTH people names AND *detailed* ministerial portfolio descriptions, it MUST be classified as Hybrid (Type 3)
- Classify as **"People" (Type 2)** if it ONLY mentions personnel changes (appointments, retirements, promotions, transfers) **without detailed breakdown of portfolio responsibilities**
- Classify as **"Organisational" (Type 1)** if it ONLY mentions structural or administrative changes **with no specific individuals named**

---

1. **Organisational Gazettes** (Type 1): ONLY government structural/administrative changes (NO specific people named)
   - Assignment of functions and duties to ministries/departments
   - Restructuring, renaming, merging, or dissolving ministries/departments
   - Portfolio changes without naming who holds them
   - Changing ministerial portfolios without naming individuals

2. **People Gazettes** (Type 2): ONLY government personnel changes (NO detailed portfolio responsibilities)
   - Appointments, resignations, transfers, promotions, retirements
   - Mentions of named individuals with **basic titles only** (e.g., "appointed as Prime Minister")
   - **DOES NOT include** descriptions of what the person is responsible for in terms of subject areas

3. **Hybrid Gazettes** (Type 3): BOTH people and detailed portfolio responsibilities present
   - Names a specific individual (including the President, Prime Minister, or other office holders) AND clearly outlines the portfolios or responsibilities they hold, Even if a formal name is not provided, assigning ministries to a known office (e.g., "the President") counts as naming a person
   - Mentions *both* who is being appointed and *what areas* (e.g., "Minister of Finance, responsible for Treasury, Economic Planning, and Public Accounts")
   - Includes **both** the individual’s name/title AND **detailed subject matter responsibility**
   - Contains both "who" (government person) and "what" (detailed government responsibilities/portfolios)

⚠️ **Clarification Example**:
- "Hon. Harini Amarasuriya appointed as Prime Minister" → **Type 2 (People)**  
   *(Only a title, no detailed portfolio explanation)*
- "Hon. Harini Amarasuriya appointed Minister of Social Empowerment, in charge of child development, elderly care, and women's welfare" → **Type 3 (Hybrid)**
- "Ministry of Energy to handle national grid operations, tourism shifted under Economic Affairs" → **Type 1 (Organisational)**  
   *(Structural change only, no specific person named)*
- "The President is assigned the Ministry of Finance, Energy, and Agriculture" → **Type 3 (Hybrid)**  
   *(Named individual with multiple portfolios assigned)*

---

**CRITICAL DECISION RULES:**
1. **First Check**: Is this about government structure/personnel? If NO → "NOT APPLICABLE"
2. **If Government-Related**: 
   - Names + *detailed responsibilities* → Hybrid (Type 3)
   - Only names with general titles → People (Type 2)
   - Only structural or administrative changes → Organisational (Type 1)
   - Only government structural changes with no people named → Organisational (Type 1)
   - Only government personnel with basic titles → People (Type 2)  
   - People names WITH detailed ministerial portfolios → ALWAYS Hybrid (Type 3)

---

**Instructions:**
- First determine if content relates to government structure/personnel
- If not government-related, respond with "NOT APPLICABLE - Non-governmental content"
- If government-related, analyze and classify using the three types
- Respond with the type number (1, 2, 3, or NOT APPLICABLE) followed by brief explanation

**Document ID:** {doc_id}

**Gazette Content:**
{content}

**Response Format:**
Type: [1/2/3/NOT FOUND]  
Reasoning: [Brief explanation of why this classification was chosen]
"""
