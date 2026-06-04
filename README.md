# Sentiment-Analysis-Across-Genres
Comparing Sentiment Analysis Across Literary and Social Media Texts

This project compares how the VADER sentiment analyzer behaves when applied to two very different types of text:

- **Classical literature**: three chapters from *Alice’s Adventures in Wonderland*  
- **Contemporary online discourse**: Reddit comments about the film *Notting Hill*

The goal is to show that VADER’s sentiment scores—especially the **compound** score—behave differently depending on genre, and that literary prose often receives unexpectedly high positive values.

---

## 1. Motivation

VADER is optimized for short, informal, social‑media‑like text.  
When applied to classical literature, however, it frequently produces inflated positivity.  
This project demonstrates:

- why VADER overestimates positivity in literary prose,
- how its heuristics align better with Reddit comments,
- and why genre awareness matters in sentiment analysis.

---

## 2. Data

### 2.1 Alice’s Adventures in Wonderland
Three chapters were selected:

- *Down the Rabbit Hole*  
- *Mad Tea Party*  
- *Queen’s Croquet Ground*

Each chapter is processed as a single text block.

### 2.2 Reddit Comments
A plain‑text file of user comments about *Notting Hill*, one comment per line. The comments were collected manually (not via an API or scraping tool).

**Note on data cleaning:**  
The three chapters from *Alice’s Adventures in Wonderland* were cleaned and prepared before analysis, while the Reddit comments were used in their raw form without additional preprocessing. For user‑generated content such as Reddit comments, cleaning is typically avoided because punctuation (e.g., exclamation marks), capitalization, emojis, and other informal markers carry important sentiment signals. Removing them would distort the emotional cues that VADER is designed to detect.



---

## 3. Methodology

### 3.1 VADER on Alice (chapter-level)

Each chapter is read as a full document and passed to VADER:

```python
scores = sia.polarity_scores(text)

This produces one sentiment profile per chapter:

- `pos`
- `neg`
- `neu`
- `compound`

---

### 3.2 VADER on Reddit (comment-level)
Reddit comments are processed line by line:

scores = sia.polarity_scores(comment)

Each comment is classified as:

- positive (compound > 0.05)

- negative (compound < -0.05)

- neutral (otherwise)

---

## 4. Results
### 4.1 VADER on Alice

| Chapter | Positive | Negative | Neutral | Compound | Classification |
|----------|----------|----------|----------|----------|----------|
| Down the Rabbit Hole | 0.104 | 0.073 | 0.823 | 0.9977 | Positive |
| A Mad Tea-Party | 0.072 | 0.068 | 0.860 | 0.9562 | Positive |
| The Queen's Croquet Ground | 0.099 | 0.079 | 0.822 | 0.9970 | Positive |

---

### 4.2 VADER on Reddit Comments

| Sentiment | Count |
| --- | --- |
| Positive | 27 |
| Negative | 9 |
| Neutral | 3 |

---

## 5. Interpretation

All three Alice chapters were classified as positive, whereas Reddit comments were distributed across positive, negative, and neutral categories.

### 5.1 Why VADER inflates positivity in literature

VADER was designed for modern, informal English. Literary prose contains:

- archaic vocabulary interpreted as positive (e.g., *curious*, *remarkable*, *wonderful*)
- descriptive narration mistaken for emotional positivity
- long passages that dilute negative cues
- dialogue that appears neutral but lexically “positive”

As a result, VADER assigns unusually high compound scores to classical texts.

### 5.2 Why Reddit comments behave as expected

Reddit comments:

- are short and opinionated
- contain explicit sentiment markers
- use intensifiers, negations, and colloquial tone
- match VADER’s training domain

Thus, the sentiment distribution is more balanced and intuitive.

---

## 6. Limitations of VADER

- **Lexicon mismatch** with older or literary English  
- **Context blindness** (cannot detect irony, narrative distance, or subtle emotion)  
- **Length effects** (long texts skew toward neutrality or positivity)  
- **Genre bias** (descriptive prose appears positive)

---

## 7. Future Work

- Compare VADER with transformer-based sentiment models  
- Apply sentence-level analysis to *Alice*  
- Explore sarcasm detection in Reddit comments  
- Build a custom lexicon for literary English

---

## 8. Summary

This project shows that VADER is not genre‑agnostic.  
It performs well on Reddit comments but produces inflated positivity when applied to classical literature.  
Understanding these limitations is essential when choosing sentiment tools for NLP tasks.


