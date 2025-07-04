def classify_domain(query):
    query_lower = query.lower()

    def match_keywords(keywords):
        return any(keyword.lower() in query_lower for keyword in keywords)

    if match_keywords([
        "legal documents", "case law", "statutes", "contracts", "regulations",
        "legal reasoning", "law firm", "court ruling", "jurisprudence", "compliance",
        "legal research", "legal dataset", "legal classification", "legal entity recognition",
        "legal NLP", "judicial opinion", "legal argument mining", "legal analytics",
        "AI in law", "automated legal summarization"
    ]):
        return "legal"

    elif match_keywords([
        "medical records", "clinical notes", "electronic health records", "EHR",
        "diagnosis prediction", "medical imaging", "radiology reports", "symptom classification",
        "drug discovery", "disease detection", "biomedical NLP", "healthcare analytics",
        "medical dataset", "patient data", "clinical trials", "medical entity recognition",
        "health informatics", "AI in medicine", "treatment recommendation", "automated medical summarization"
    ]):
        return "medical"

    elif match_keywords([
        "academic research", "scientific papers", "research paper analysis", "literature review automation",
        "citation prediction", "topic modeling", "research trend analysis", "NLP in academia",
        "academic recommender systems", "arXiv dataset", "Semantic Scholar", "knowledge graph",
        "co-authorship networks", "scientific impact metrics", "scholarly data mining", "AI for science",
        "university research", "paper summarization", "academic corpus", "research dataset"
    ]):
        return "academic"

    elif match_keywords([
        "Yahoo Finance API", "yfinance", "stock price prediction", "financial time series",
        "historical market data", "real-time stock data", "machine learning in finance",
        "trend analysis", "portfolio optimization", "Quandl", "economic indicators",
        "macroeconomic forecasting", "asset pricing models", "financial risk modeling",
        "data API", "Python finance datasets", "Alpaca API", "algorithmic trading",
        "reinforcement learning", "paper trading", "market simulation", "real-time trading data",
        "AI trading bots"
    ]):
        return "finance"

    elif match_keywords([
        "Magenta", "TensorFlow music", "AI music generation", "MelodyRNN", "MusicVAE",
        "MIDI dataset", "generative music models", "music composition AI", "NSynth",
        "sound synthesis", "timbre transfer", "instrument classification", "audio dataset",
        "neural synthesizer", "pitch and timbre features", "Spotify Web API", "music metadata",
        "audio features", "recommendation system", "playlist generation", "music mood classification",
        "user behavior modeling"
    ]):
        return "music"

    else:
        return "general"