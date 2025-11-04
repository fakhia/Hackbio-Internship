{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNNG1MpnlvVlLpNF/Jjcq42",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/fakhia/Hackbio-Internship/blob/main/simple_code.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "063a1799",
        "outputId": "f787870e-c71b-47cf-faf2-25b9634da9ad"
      },
      "source": [
        "\"\"\"\n",
        "hackbio internship - Stage 0 task\n",
        "Team : Aspartic acid\n",
        "\n",
        "#Team\n",
        "#How to write python codes for printing name, slack username,\n",
        "#country, github, linkedin, gene of interest\n",
        "#and nucleotide sequence of gene of interest\n",
        "#Author Fakhia\n",
        "#Linkedin: www.linkedin.com/in/fakiha-ch-a9aa9b270/\n",
        "#Github: https://github.com/fakhia\n",
        "\"\"\"\n",
        "#Create a list of dictionaries for  info of aspartic_acid_team\n",
        "team_aspartic_acid_info=[\n",
        "    {\n",
        "     \"Name\": \"Fakhia Mubashir\",\n",
        "     \"Slack\": \"Fakiha Mubashir\",\n",
        "     \"Country\": \"Pakistan\",\n",
        "     \"Hobby\": \"Reading\",\n",
        "     \"Affiliation\": \"None\",\n",
        "     \"Gene\": \"TRPV6\",\n",
        "     \"Sequence\": \"GCCAATTTCAGTACGATACGGTACCATGGATCACCTGAGT\"\n",
        "    }\n",
        "] # Added closing bracket here\n",
        "\n",
        "\n",
        "# Validate DNA contains only A, T, C, G\n",
        "def validate_dna(seq):\n",
        "    if seq is None:\n",
        "        return False\n",
        "    valid = {\"A\", \"T\", \"C\", \"G\"}\n",
        "    return set(seq.upper()).issubset(valid)\n",
        "\n",
        "# Calculate GC content\n",
        "def gc_content(seq):\n",
        "    g = seq.count(\"G\")\n",
        "    c = seq.count(\"C\")\n",
        "    return round((g + c) / len(seq) * 100, 2)\n",
        "\n",
        "# Print results\n",
        "# Iterate through each team member and print their details\n",
        "for member in team_aspartic_acid_info:\n",
        "    seq = member[\"Sequence\"]\n",
        "    print(f\"\\nName: {member['Name']}\")\n",
        "    print(f\"Slack: {member['Slack']}\")\n",
        "    print(f\"Country: {member['Country']}\")\n",
        "    print(f\"Hobby: {member['Hobby']}\")\n",
        "    print(f\"Affiliation: {member['Affiliation']}\")\n",
        "    print(f\"Favorite Gene: {member['Gene']}\")\n",
        "\n",
        "    if validate_dna(seq):\n",
        "        print(f\"GC Content: {gc_content(seq)}%\")\n",
        "    else:\n",
        "        print(\"GC Content: N/A (Invalid or no DNA sequence)\")"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "Name: Fakhia Mubashir\n",
            "Slack: Fakiha Mubashir\n",
            "Country: Pakistan\n",
            "Hobby: Reading\n",
            "Affiliation: None\n",
            "Favorite Gene: TRPV6\n",
            "GC Content: 47.5%\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\"\"\"\n",
        "HackBio Internship — Stage 0 Task\n",
        "Team: Leucine\n",
        "\n",
        "# Task:\n",
        "# Write a simple Python script for printing the names, Slack username,\n",
        "# country, one hobby, affiliations of people on your team,\n",
        "# and the DNA sequence of the genes they love most.\n",
        "# Author: Fakhia Mubashir\n",
        "# GitHub: https://github.com/fakhia\n",
        "# LinkedIn: www.linkedin.com/in/fakiha-ch-a9aa9b270/\n",
        "\"\"\"\n",
        "# Created a list of dictionaries for team_aspartic_acid_info\n",
        "team_aspartic_acid_info = [\n",
        "    {\n",
        "    \"Name\":\"Fakhia Mubashir\",\n",
        "    \"Slack\": \"Fakhia Mubashir\",\n",
        "    \"Country\": \"Pakistan\",\n",
        "    \"Hobby\": \"Writing\",\n",
        "    \"Affiliation\": \"None\",\n",
        "    \"Gene\": \"TRPV6\",\n",
        "    \"Sequence\": \"GCTGAGACTTCCTGGACGCCAATTACCGGGGACAGGCTGTGGGGTTTCTCAGATAACTGGGCCCCTGCGCTCAGGAGGC\"\n",
        "}\n",
        "] # Added closing bracket here\n",
        "\n",
        "\n",
        "# Validate DNA contains only A, T, C, G\n",
        "def validate_dna(seq):\n",
        "    if seq is None:\n",
        "        return False\n",
        "    valid = {\"A\", \"T\", \"C\", \"G\"}\n",
        "    return set(seq.upper()).issubset(valid)\n",
        "\n",
        "# Calculate GC content\n",
        "def gc_content(seq):\n",
        "    g = seq.count(\"G\")\n",
        "    c = seq.count(\"C\")\n",
        "    return round((g + c) / len(seq) * 100, 2)\n",
        "\n",
        "# Print results\n",
        "# Iterate through each team member and print their details\n",
        "for member in team_aspartic_acid_info:\n",
        "    seq = member[\"Sequence\"]\n",
        "    print(f\"\\nName: {member['Name']}\")\n",
        "    print(f\"Slack: {member['Slack']}\")\n",
        "    print(f\"Country: {member['Country']}\")\n",
        "    print(f\"Hobby: {member['Hobby']}\")\n",
        "    print(f\"Affiliation: {member['Affiliation']}\")\n",
        "    print(f\"Favorite Gene: {member['Gene']}\")\n",
        "\n",
        "    if validate_dna(seq):\n",
        "        print(f\"GC Content: {gc_content(seq)}%\")\n",
        "    else:\n",
        "        print(\"GC Content: N/A (Invalid or no DNA sequence)\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cUUq0gBrxiT6",
        "outputId": "27fa786a-c397-431d-de44-8e6fba38454e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "Name: Fakhia Mubashir\n",
            "Slack: Fakhia Mubashir\n",
            "Country: Pakistan\n",
            "Hobby: Writing\n",
            "Affiliation: None\n",
            "Favorite Gene: TRPV6\n",
            "GC Content: 62.03%\n"
          ]
        }
      ]
    }
  ]
}