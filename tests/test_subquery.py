import pytest
from subquery import SubqueryResult


def test_subquery_result():
    result = SubqueryResult(follow_up=["What's the population?"], subquery=["Paris France capital"])
    assert isinstance(result.follow_up, list)
    assert isinstance(result.subquery, list)
    assert len(result.follow_up) > 0
    assert len(result.subquery) > 0


@pytest.mark.transformers
def test_transformers_subquery_generator():
    from subquery import TransformersSubqueryGenerator

    generator = TransformersSubqueryGenerator()
    result = generator.generate("Who founded the last winner of premier league?")

    assert isinstance(result, SubqueryResult)
    assert isinstance(result.follow_up, list)
    assert isinstance(result.subquery, list)
    assert len(result.follow_up) > 0 or len(result.subquery) > 0


@pytest.mark.ollama
def test_ollama_subquery_generator():
    from subquery import OllamaSubqueryGenerator

    generator = OllamaSubqueryGenerator()
    result = generator.generate("What is this?")

    assert isinstance(result, SubqueryResult)
    assert isinstance(result.follow_up, list)
    assert isinstance(result.subquery, list)
    assert len(result.follow_up) > 0 or len(result.subquery) > 0